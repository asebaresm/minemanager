#from minemanager.lib.helpers.aux import load_yaml
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# These attributes are defined here as entry points to the app
CONFIG_FILE    = os.path.join(ROOT, 'config', 'config.yml')
PRIVATE_FILE   = os.path.join(ROOT, 'private', 'private.yml')
BACK_UPS       = os.path.join(ROOT, 'bak')

# Some general constants
STAT_OK, STAT_ERR,  STAT_UNKN = range(3)
NMAP_UP, NMAP_DOWN, NMAP_UNKN = range(3)

A_STATUS =    {
                STAT_OK :  'OK. ☀',
                STAT_ERR:  'ERR 🌧',
                STAT_UNKN: 'UNK 🌥'
              }

NMAP_STATUS = {
                NMAP_UP :  'UP ☀',
                NMAP_DOWN: 'DOWN 🌧',
                NMAP_UNKN: 'UNKN 🌥'
              }

VALIDATE_NMAP = re.compile(r"Nmap done: \d+ IP address (\(\d+ host(?:s)? up\)) scanned in \d+\.\d+ seconds")
VALIDATE_IP   = re.compile(r"\d+\.\d+\.\d+\.\d+")
IS_MINER      = re.compile(r"miner\d+")

RL_SYNC  = 'sync'
RL_RESET = 'reset'
