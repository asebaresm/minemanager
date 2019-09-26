#from minemanager.lib.helpers.aux import load_yaml
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# These attributes are defined here as entry points to the app
CONFIG_FILE    = os.path.join(ROOT, 'config', 'config.yml')
PRIVATE_FILE   = os.path.join(ROOT, 'private', 'private.yml')
BACK_UPS       = os.path.join(ROOT, 'bak')

# load configs
#SUPPORT        = load_yaml(CONFIG_FILE)['bot_info']['support']
#PROJECTS       = load_yaml(PRIVATE_FILE)['company']['projects']
