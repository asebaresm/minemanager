from minemanager import definitions as defs
from minemanager.lib.helpers import aux

import re
import subprocess

VALIDATE_NMAP = re.compile(r"Nmap done: \d+ IP address (\(\d+ host(?:s)? up\)) scanned in \d+\.\d+ seconds")
VALIDATE_IP   = re.compile(r"\d+\.\d+\.\d+\.\d+")

# Returns:
#   UP   - nmap returned (1 hosts up)
#   DOWN - nmap returned (0 hosts up)
#   UNKN - nmap result didn't match expected output
def host_status(host):
    nmap_lines = ping_host(host)
    result = nmap_lines[-1]
    if not aux.does_match(result, VALIDATE_NMAP):
        return defs.NMAP_UNKN
    status = aux.extract_one(result, VALIDATE_NMAP)
    if status == '(1 host up)':
        return defs.NMAP_UP
    elif status == '(0 hosts up)':
        return defs.NMAP_DOWN
    else:
        return defs.NMAP_UNKN

def host_2_relay(host):
    hosts = aux.load_hosts()
    return hosts.get(host, host)['relay']

def resolve_host(host):
    hosts = aux.load_hosts()
    if aux.does_match(host, VALIDATE_IP):
        return host
    return hosts.get(host, host)['ip']

def ping_host(host):
    nmap_out = subprocess.run(
        args = ['nmap', '-sP', resolve_host(host), '--max-rtt-timeout', '100ms'],
        universal_newlines = True,
        stdout = subprocess.PIPE
    )
    nmap_lines = nmap_out.stdout.splitlines()
    return nmap_lines

def main():
    print(host_status('miner58'))

if __name__ == '__main__':
    main()
