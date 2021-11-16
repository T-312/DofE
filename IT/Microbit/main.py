# from microbit import *
import radio
import time, random

def next_slide():
    if button_a.is_pressed():
        pass

def prev_slide():
    if button_b.is_pressed():
        pass

def start_or_exit(current_status):
    if button_a.is_pressed() and button_b.is_pressed():
        if current_status:
            pass

        else:
            pass

def start_bluetooth():
    radio.on()

def stop_bluetooth():
    radio.off()