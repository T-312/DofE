from microbit import *
import radio, time, random, threading

class MicroBit:
    def __init__(self):
        self.succesful_connection = Image('00000:'
                                     '00009:'
                                     '00090:'
                                     '90900:'
                                     '09000')

        radio.config(channel=10, group=0, power=7, data_rate=radio.RATE_2MBIT)
        radio.on()

    def recieve():
        incoming = radio.receive_full()
        if incoming:
            msg, rssi, timestamp = incoming
            msg = str(msg, 'utf-8')[-1]
            return msg

    def a_pressed():
        return button_a.was_pressed()

    def b_pressed():
        return button_b.was_pressed()

    def succesful_connection():
        return self.succesful_connection

def main():
    running = True

    while running:
        while True:
            radio.send("conn")
            if MicroBit.recieve() == "conn":
                display.show(MicroBit.succesful_connection())
                time.sleep(0.5)
                display.clear()
                break
        
        if MicroBit.b_pressed():
            

if __name__ == "__main__":
    main()