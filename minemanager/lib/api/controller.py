from minemanager import definitions
from minemanager.lib.helpers import aux
from minemanager.lib.helpers import checks
from minemanager.lib.raspi import relayboard

# STATES after running an action:
# - STAT_OK:  sequence ended as expected
# - STAT_ERR: error at a code level. This should not happen
#             (e.g. invalid hostname, invalid action for host)
class HostController:
    def __init__(self):
        self.rb = relayboard.RelayBoard()

    def reboot(self, host):
        re, type = aux.host_relay(host)
        if re is None:
            return definitions.STAT_ERR # invalid host
        if type == definitions.RL_SYNC:
            if self.rb.powercycle(re):
                return definitions.STAT_OK
            else:
                return definitions.STAT_UNKN
        else:
            if self.rb.reset(re):
                return definitions.STAT_OK
        return definitions.STAT_UNKN

    def shutdown(self, host):
        re, type = aux.host_relay(host)
        if re is None:
            return definitions.STAT_ERR # invalid host
        if type == definitions.RL_SYNC:
            if self.rb.poweroff(re):
                return definitions.STAT_OK
            else:
                return definitions.STAT_UNKN
        return definitions.STAT_ERR # invalid action, undef

    def boot(self, host):
        re, type = aux.host_relay(host)
        if re is None:
            return definitions.STAT_ERR # invalid host
        if type == definitions.RL_SYNC:
            if self.rb.poweron(re):
                return definitions.STAT_OK
            else:
                return definitions.STAT_UNKN
        return definitions.STAT_ERR # invalid action, undef
