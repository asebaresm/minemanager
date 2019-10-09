from minemanager import definitions
from shutil import copyfile

import os
import re
import time
import yaml

def back_up_file(src):
    dst = definitions.BACK_UPS \
          + os.sep + src.split('/')[-1] \
          + '.'    + str(int(time.time()))
    copyfile(src, dst)

def load_yaml(fname):
    with open(fname, 'r') as f:
        return yaml.safe_load(f)

def save_yaml(fname, data):
    back_up_file(fname)
    with open(fname, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def does_match(str, exp):
    if exp.match(str):
        return True
    return False

# Extract 1 field from the argument pattern and string
# A valid python regex is expected as pattern
def extract_one(str, pattern):
    match = re.search(pattern,str)
    if match:
        return match.group(1)
    return None

# Extract 2 fields from the argument pattern and string
def extract_two(str, pattern):
    match = re.search(pattern,str)
    if match:
        return match.group(1), match.group(2)
    return None, None

def load_whitelist():
    priv = load_yaml(definitions.PRIVATE_FILE)
    return priv['mod']['email_whitelist']

def load_users():
    priv = load_yaml(definitions.PRIVATE_FILE)
    return priv['mod']['users']

def load_hosts():
    priv = load_yaml(definitions.PRIVATE_FILE)
    return priv['hosts']

def load_god():
    priv = load_yaml(definitions.PRIVATE_FILE)
    return priv['mod']['god']

def store_users(users):
    priv = load_yaml(definitions.PRIVATE_FILE)
    priv['mod']['users'] = users
    save_yaml(definitions.PRIVATE_FILE, priv)

def append_data(data):
    db = load_yaml(definitions.DATA_FILE)
    save_yaml(definitions.DATA_FILE, merge(db, data))

def dump_data():
    #user_data = load_yaml(definitions.DATA_FILE)[user]
    with open(definitions.DATA_FILE, 'r') as f:
        return yaml.dump(yaml.safe_load(f), default_flow_style=False)

def dump_user_data(user):
    #user_data = load_yaml(definitions.DATA_FILE)[user]
    with open(definitions.DATA_FILE, 'r') as f:
        return yaml.dump(yaml.safe_load(f)[user], default_flow_style=False)

def host_relay(h):
    hosts = load_hosts()
    name = get_hostname(h)
    if name is None:
        return None, None # host not found, invalid host
    return hosts[name]['relay'], hosts[name]['type']

def get_hostname(name):
    hosts = load_hosts()
    if hosts.get(name):
        return name
    for host in hosts.keys():
        if name == hosts[host]['ip']:
            return host
    return None

def resolve_host(host):
    hosts = load_hosts()
    if does_match(host, definitions.VALIDATE_IP):
        return host
    return hosts.get(host, host)['ip']

# Monkey-patch Python dict
# Policy: a mutates. Contents of b are added to a and returns a
def merge(a, b, path=None):
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a
