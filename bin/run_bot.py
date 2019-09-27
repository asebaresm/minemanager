
from minemanager import definitions
from minemanager.lib.helpers import chat
from minemanager.lib.helpers import checks
from minemanager.lib.helpers.aux import load_yaml
from minemanager.lib.mod.users import register_user, active_user
from minemanager.lib.raspi import relayboard

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext import (Updater, CommandHandler, InlineQueryHandler,
                          MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging
import os
import re
import signal
import subprocess
import sys
import time

class MineBot(object):
    def __init__(self,config_name, credentials_name):
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.config = load_yaml(config_name)
        self.credentials = load_yaml(credentials_name)
        self.logger = logging.getLogger(__name__)
        self.relayboard = relayboard.RelayBoard()

    def start(self, bot, update):
        uid = update.message.from_user.id
        self.logger.info('/start issued by "%s"', uid)

        if not active_user(uid):
            update.message.reply_text(chat.SIGNUP_PLS, reply_markup=ReplyKeyboardRemove())
            return chat.GO_SIGNUP
        update.message.reply_text(chat.START_GREET)
        return chat.MAIN_MENU

    def help(self, bot, update):
        """Send a message when the command /help is issued."""
        self.logger.info('/help issued by "%s"', update.message.from_user.id)
        update.message.reply_text(chat.HELP_GLOBAL, reply_markup=ReplyKeyboardRemove())
        return None

    def restart(self, bot, update, args):
        self.logger.info('/reboot issued by "%s"', update.message.from_user.id)
        txt = "\nRebooting %s..." % args[0]
        update.message.reply_text(txt)
        host_relay = checks.host_2_relay(args[0])
        self.relayboard.powercycle(host_relay)
        update.message.reply_text("\nDone")
        return None

    def poweron(self, bot, update, args):
        self.logger.info('/poweron issued by "%s"', update.message.from_user.id)
        txt = "\nPowering on %s..." % args[0]
        update.message.reply_text(txt)
        host_relay = checks.host_2_relay(args[0])
        self.relayboard.poweron(host_relay)
        update.message.reply_text("\nDone")
        return None

    def poweroff(self, bot, update, args):
        self.logger.info('/poweroff issued by "%s"', update.message.from_user.id)
        txt = "\nPowering off %s..." % args[0]
        update.message.reply_text(txt)
        host_relay = checks.host_2_relay(args[0])
        self.relayboard.poweroff(host_relay)
        update.message.reply_text("\nDone")
        return None

    def halt_handler(self, sig, frame):
        print("CTRL+C pressed., stopping %s" % self.config['bot_info']['name'])
        sys.exit(0)

    def error(update, context):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    minebot = MineBot(definitions.CONFIG_FILE, definitions.PRIVATE_FILE)
    updater = Updater(token=minebot.credentials['credentials']['token'],user_sig_handler=minebot.halt_handler)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", minebot.help))
    dp.add_handler(CommandHandler("poweroff", minebot.poweroff, pass_args=True))
    dp.add_handler(CommandHandler("poweron", minebot.poweron, pass_args=True))
    dp.add_handler(CommandHandler("restart", minebot.restart, pass_args=True))
    dp.add_handler(CommandHandler("start", minebot.start))
    dp.add_error_handler(minebot.error)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    updater.stop()

if __name__ == '__main__':
    main()
