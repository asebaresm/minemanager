# Relay handling using the GPIO
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

CHAN_LIST = [22, 29, 32, 31, 33, 36, 37]

RELAYS = {
            1: CHAN_LIST[0],
            2: CHAN_LIST[1],
            3: CHAN_LIST[2],
            4: CHAN_LIST[3],
            5: CHAN_LIST[4],
            6: CHAN_LIST[5],
            7: CHAN_LIST[6]
         }

class RelayBoard:

    def __init__(self):
        GPIO.setup(CHAN_LIST, GPIO.OUT, initial=GPIO.HIGH)

    def pwrcycle(self, relay, t):
        GPIO.output(RELAYS[relay], False)
        time.sleep(t)
        GPIO.output(RELAYS[relay], True)


def main():
    time.sleep(2)
    rb = RelayBoard()
    for r in [1,2,3,4,5,6,7]:
        rb.pwrcycle(r, 0.5)

if __name__ == '__main__':
    main()

