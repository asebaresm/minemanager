#from minemanager.lib.helpers.aux import load_yaml
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# These attributes are defined here as entry points to the app
CONFIG_FILE    = os.path.join(ROOT, 'config', 'config.yml')
PRIVATE_FILE   = os.path.join(ROOT, 'private', 'private.yml')
BACK_UPS       = os.path.join(ROOT, 'bak')

# Some general cons

NMAP_UP, NMAP_DOWN, NMAP_UNKN = range(3)

nmap_status = {
                NMAP_UP : 'UP',
                NMAP_DOWN: 'DOWN',
                NMAP_UNKN: 'UNKN'
              }
