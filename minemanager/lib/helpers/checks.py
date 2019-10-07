from minemanager import definitions
from minemanager.lib.helpers import aux

import re
import subprocess

# Returns:
#   UP   - nmap returned (1 hosts up)
#   DOWN - nmap returned (0 hosts up)
#   UNKN - nmap result didn't match expected output
def host_status(host):
    nmap_lines = ping_host(host)
    result = nmap_lines[-1]
    if not aux.does_match(result, definitions.VALIDATE_NMAP):
        return definitions.NMAP_UNKN
    status = aux.extract_one(result, definitions.VALIDATE_NMAP)
    if status == '(1 host up)':
        return definitions.NMAP_UP
    elif status == '(0 hosts up)':
        return definitions.NMAP_DOWN
    else:
        return definitions.NMAP_UNKN

def ping_host(host):
    nmap_out = subprocess.run(
        args = ['nmap', '-sP', aux.resolve_host(host), '--max-rtt-timeout', '100ms'],
        universal_newlines = True,
        stdout = subprocess.PIPE
    )
    nmap_lines = nmap_out.stdout.splitlines()
    return nmap_lines

def main():
    print(host_status('miner58'))

if __name__ == '__main__':
    main()
