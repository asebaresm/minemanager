from minemanager.aux import load_yaml, save_yaml

CONFIG_FILE = 'config/config.yml'
PRIVATE_FILE = 'private/private.yml'

def load_whitelist():
    priv = load_yaml(paths.PRIVATE_FILE)
    return priv['mod']['email_whitelist']

def load_users():
    priv = load_yaml(paths.PRIVATE_FILE)
    return priv['mod']['users']

def store_users(users):
    priv = load_yaml(paths.PRIVATE_FILE)
    priv['mod']['users'] = users
    save_yaml(PRIVATE_FILE, priv)
