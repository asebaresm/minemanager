# Relay handling using the GPIO
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# - 2 channels are allocated by default for each relay, input & output
# - Usage of input channels is determined by the reboot policy: reset/sync
# sync:  powercycles the host in a synchronous manner
# reset: simply send reset signal to board panel
IN_CHN_LIST  = [12, 11, 13, 16, 15, 18]
OUT_CHN_LIST = [29, 32, 31, 33, 36, 37]

RELAYS = {
            1: { 'in': IN_CHN_LIST[0], 'out': OUT_CHN_LIST[0] },
            2: { 'in': IN_CHN_LIST[1], 'out': OUT_CHN_LIST[1] },
            3: { 'in': IN_CHN_LIST[2], 'out': OUT_CHN_LIST[2] },
            4: { 'in': IN_CHN_LIST[3], 'out': OUT_CHN_LIST[3] },
            5: { 'in': IN_CHN_LIST[4], 'out': OUT_CHN_LIST[4] },
            6: { 'in': IN_CHN_LIST[5], 'out': OUT_CHN_LIST[5] },
         }

class RelayBoard:

    def __init__(self):
        GPIO.setup(OUT_CHN_LIST, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(IN_CHN_LIST, GPIO.IN)

    def powercycle(self, relay):
        self.poweroff(relay)
        # wait 0.5s to end power-off
        time.sleep(3)
        if not self.poweron(relay):
            return False
        return True

    def poweron(self, relay):
        if GPIO.input(RELAYS[relay]['in']) == GPIO.HIGH:
            return False
        # Press power and wait for PLED to go HIGH
        GPIO.output(RELAYS[relay]['out'], GPIO.LOW)
        while GPIO.input(RELAYS[relay]['in']) == GPIO.LOW:
            time.sleep(0.02) # 20ms
        GPIO.output(RELAYS[relay]['out'], GPIO.HIGH)
        return True

    def poweroff(self, relay):
        if GPIO.input(RELAYS[relay]['in']) == GPIO.LOW:
            return False
        # Press power and wait for PLED to go LOW
        GPIO.output(RELAYS[relay]['out'], GPIO.LOW)
        while GPIO.input(RELAYS[relay]['in']) == GPIO.HIGH:
            time.sleep(0.02)
        GPIO.output(RELAYS[relay]['out'], GPIO.HIGH)
        return True

    def reset(self, relay):
        if GPIO.output(RELAYS[relay]['out'], GPIO.LOW):
            return False
        GPIO.output(RELAYS[relay]['out'], GPIO.LOW)
        time.sleep(2)
        if GPIO.output(RELAYS[relay]['out'], GPIO.HIGH):
            return False
        GPIO.output(RELAYS[relay]['out'], GPIO.HIGH)
        return True

def main():
    time.sleep(2)
    print("\nGO!")
    rb = RelayBoard()
    rb.powercycle(1)

if __name__ == '__main__':
    main()
