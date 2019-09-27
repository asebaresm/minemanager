# Relay handling using the GPIO
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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

        self.poweron(relay)

    def poweron(self, relay):
        # Press power and wait for PLED to go HIGH
        GPIO.output(RELAYS[relay]['out'], GPIO.LOW)
        while GPIO.input(RELAYS[relay]['in']) == GPIO.LOW:
            time.sleep(0.02)
        GPIO.output(RELAYS[relay]['out'], GPIO.HIGH)

    def poweroff(self, relay):
        # Press power and wait for PLED to go LOW
        GPIO.output(RELAYS[relay]['out'], GPIO.LOW)
        while GPIO.input(RELAYS[relay]['in']) == GPIO.HIGH:
            time.sleep(0.02)
        GPIO.output(RELAYS[relay]['out'], GPIO.HIGH)

def main():
    time.sleep(2)
    print("\nGO!")
    rb = RelayBoard()
    rb.powercycle(1)

if __name__ == '__main__':
    main()
