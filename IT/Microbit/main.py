from microbit import *
import radio
import time, random

def start_radio():
    radio.config(channel=10)
    radio.on()

def stop_radio():
    radio.off()
    exit()

def send_msg(msg):
    radio.send(msg)

def recieved():
    incoming = radio.recieve()
    if incoming == "next":
        print("Next")

    if incoming == "prev":
        print("Previous")

def a_pressed():
    return button_a.was_pressed()

def b_pressed():
    return button_b.was_pressed()

def both_pressed(current_status):
    if button_a.is_pressed() and button_b.is_pressed():
        if current_status:
            stop_radio()

def main():
    start_radio()
    running = True
    while running:
        if a_pressed():
            radio.send("prev")

        if b_pressed():
            radio.send("next")

        recieved()
        both_pressed(running)
        time.sleep(1)

if __name__ == "__main__":
    main()
