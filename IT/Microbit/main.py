# Try using this for help: https://microbit-micropython.readthedocs.io/en/v1.0.1/radio.html

from microbit import *
import radio, threading
import time, random

class MicroBit:
    def __init__(self):
        self = MicroBit.__init__()

    def start_radio():
        print("Starting radio...")
        radio.config(channel=10, group=0, power=7, data_rate=radio.RATE_2MBIT)
        radio.on()

    def stop_radio():
        print("Stopping radio")
        radio.off()
        exit()

    def pair():
        incoming = radio.receive_full()
        if incoming:
            msg, rssi, timestamp = incoming
            msg = str(msg, 'utf-8')[3:]
            if msg == "conn":
                return True

        return False

    def rec_num():
        incoming = radio.receive_full()
        if incoming:
            msg, rssi, timestamp = incoming
            msg = str(msg, 'utf-8')[-1]
            return msg

    def a_pressed():
        return button_a.was_pressed()

    def b_pressed():
        return button_b.was_pressed()

    def gen_rnd_num(start_point, end_point):
        return random.randrange(start_point, end_point)

    def connected():
        display.show(Image('00000:'
                           '00009:'
                           '00090:'
                           '90900:'
                           '09000'))

        time.sleep(0.5)
        display.clear()

def main():
    MicroBit.start_radio()
    running = True
    connected = False

    while running:
        if MicroBit.a_pressed() and not connected:
            radio.send("conn")

        if MicroBit.pair() and not connected:
            MicroBit.connected()
            connected = True

        if MicroBit.b_pressed() and connected:
            pass

if __name__ == "__main__":
    main()