import os
import time
import colorama
from colorama import init
from colorama import Fore, Back, Style

init()

a = True
while a == True:
    r = 0
    a = input("Enter PATH: ")
    b = 0
    c = 0
    d = 0

    start = time.time()        
    for dirpath, dirnames, filenames in os.walk(a):
        b+=1
        for f in dirnames:
            c+=1
        for f in filenames:
            d+=1

    print(Fore.RED)
    print(b, " paths", sep='')
    print(c, " folders", sep='')
    print(d, " files", sep='')
    print(Style.RESET_ALL)
    stop = time.time()
    print(Fore.CYAN)
    print("Time spent: ", round(stop - start, 1), " seconds", sep='')
    print(Style.RESET_ALL)
    print(Fore.MAGENTA)
    print(round(d, 2) // round(stop - start, 2), "files per second")
    break

    #Print the choices to the user, considering where they are - dirlist() so he can enter them with numbers
    #Make a file search system - another input - if input in b, c or d print Request found!