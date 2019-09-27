# -*- coding: utf-8 -*-
from minemanager import definitions
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

import re

MAIN_MENU, GO_SIGNUP, CHOOSE_FIELD, TYPING_REPLY, CLOSE_TASK = range(5)

VALIDATE_DESC     = re.compile(r"[,\(\)&\w\s_:'\"\-]+(#minero|#portal|#other)")
VALIDATE_EMAIL    = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
VALIDATE_DATE     = re.compile(r"\d\d\d\d-\d\d-\d\d")
VALIDATE_DATE_SH  = re.compile(r"\"?(hoy|today)\"?")
VALIDATE_TIME     = re.compile(r"\d\d:\d\d")
VALIDATE_TIME_SH  = re.compile(r"\"?(now|ahora)\"?")
VALIDATE_DURATION = re.compile(r"\d+")

MAIN_KB           =   [['']]

ENTRY_KEYBOARD    =   [['']]

START_NO_SIGNUP      = "Usa el comando /signup <correo> primero para activar tu usuario."
START_GREET          = "Your face looks familiar to me. Well then, what can I do for you?"

SIGNUP_PLS           = "There's nothing here for you, go away..."
SIGNUP_INVALID_EMAIL = "Introduce un email valido"
SIGNUP_ALREADY_OK    = "Ya estabas registrado"
SIGNUP_UNAUTH        = "Ese email no esta en la whitelist.\n" \
                       "Escribe a %s para ser añadido "  \
                       "y vuelve a escribirme el email."
SIGNUP_SUCCESS = "Se ha asignado el id %s a tu email. Si cambias de cuenta \n"\
                 "tendras que volver a registrarte."

HELP_GLOBAL    = "Available CLI commands:\n"\
                 "/list            - List mapped hosts\n"\
                 "/ping <host>     - ping a host to check for its status\n"\
                 "/pingsweep       - ping every host from list\n"\
                 "/restart <host>   - Reboot the host machine\n"\
                 "/start           - \n"\
                 "/signup <correo> - signup with mail\n"\

def matches_any(str, exp_list):
    for r in exp_list:
        if r.match(str):
            return True
    return False
