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

    def pair():
        incoming = radio.receive_full()
        if incoming:
            msg, rssi, timestamp = incoming
            msg = str(msg, 'utf-8')[3:]
            if msg == "conn":
                return True

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

    def both_pressed(current_status):
        if button_a.is_pressed() and button_b.is_pressed():
            if current_status:
                MicroBit.stop_radio()

    def gen_rnd_num(start_point, end_point):
        rnd_num = random.randrange(start_point, end_point)
        return rnd_num

def main():
    MicroBit.start_radio()
    running = True
    connected = False
    while running:
        time.sleep(0.5)
        if MicroBit.a_pressed():
            radio.send("conn")

        if MicroBit.pair() and not connected:
            print("Connected")
            connected = True

        if MicroBit.b_pressed() and connected:
            n = str(MicroBit.gen_rnd_num(1, 7))
            radio.send(n)

            recn = MicroBit.rec_num()
            while recn == None:
                recn = MicroBit.rec_num()
            
            if int(n) > int(recn):
                print("Microbit 1 won!")
                display.show(n)
                display.clear()
                display.show(Image.HAPPY)

            if int(n) < int(recn):
                print("Microbit 2 won!")
                display.show(n)
                display.clear()
                display.show(Image.SAD)

            if int(n) == int(recn):
                print("Draw")
                print(recn)

if __name__ == "__main__":
    main()