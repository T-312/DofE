from microbit import *
import radio
import time, random

class MicroBit:
    def __init__(self, rnd_num):
        self.rnd_num = rnd_num

    def start_radio():
        print("Starting radio...")
        radio.config(channel=10)
        radio.on()

    def stop_radio():
        print("Stopping radio")
        radio.off()
        exit()

    def recieved():
        incoming = radio.receive_full()
        if incoming:
            msg, rssi, timestamp = incoming
            print("Recieved message")
            print(msg)
            return True

    def a_pressed():
        return button_a.was_pressed()

    def b_pressed():
        return button_b.was_pressed()

    def both_pressed(current_status):
        if button_a.is_pressed() and button_b.is_pressed():
            print("Buttons A and B was pressed!")
            if current_status:
                MicroBit.stop_radio()

    def gen_rnd_num(start_point, end_point):
        rnd_num = random.randrange(start_point, end_point)
        return rnd_num

def main():
    MicroBit.start_radio()
    running = True
    while running:
        time.sleep(0.5)
        if MicroBit.a_pressed():
            print("Button A was pressed!")
            radio.send("conn")

        if MicroBit.b_pressed():
            print("Button B was pressed!")
            print(MicroBit.gen_rnd_num(1, 7))

        if MicroBit.recieved():
            print("Recieved")

        MicroBit.both_pressed(running)
        

if __name__ == "__main__":
    main()