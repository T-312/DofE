from microbit import *
import radio
import time, random

def start_radio():
    radio.on()

def stop_radio():
    radio.off()

def a_pressed():
    if button_a.is_pressed():
        return True

def b_pressed():
    if button_b.is_pressed():
        return True

def both_pressed(current_status):
    if button_a.is_pressed() and button_b.is_pressed():
        if current_status:
            stop_radio()

        else:
            pass

def main():
    start_radio()
    running = True
    while running:
        if a_pressed():
            pass

        if b_pressed():
            pass

if __name__ == "__main__":
    main()
