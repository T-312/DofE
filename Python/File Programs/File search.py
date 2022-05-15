import os, time, threading

folders = [f.path for f in os.scandir('C:/') if f.is_dir()]
f = input("Enter file name with the extension: ")

def search_dir(dir_name):
    for dirnames, dirlist, filenames in os.walk(dir_name):
        if f in filenames:
            print(str(os.path.join(dirnames, f)).replace('\\', '/'))

threads = []

for dir_name in folders:
    t = threading.Thread(target=search_dir, args=[dir_name])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()