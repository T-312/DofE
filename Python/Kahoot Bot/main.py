#Nick for kahoot: https://unicode-explorer.com/c/200C

from KahootPY import client
import time, threading, os

pin = 5157992 #Change pin here

def start_bot(bots, i, bot_name):
    bot = client()
    bot.join(pin, bot_name + ' ' * i)
    bots.append(bot)
    print(bot)
    
def bot_leave(bot):
    bot.leave()

def start_flood(bot_num):
    bots = []
    threads = []

    for i in range(bot_num):
        t = threading.Thread(target=start_bot, args=(bots, i, 'ඞ'))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    time.sleep(3)
    threads.clear()

    for bot in bots:
        t = threading.Thread(target=bot_leave, args=[bot])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

start_flood(20)
os.system('cls||clear')