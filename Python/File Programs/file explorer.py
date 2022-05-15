import os


current_path = []
a = r'C:/'
os.chdir('')

current_path.append(a)

for f in os.listdir():
    file_name, file_ext = (os.path.splitext(f))
    print(file_name)

    what = input("Enter folder name: ")
    current_path.append(what)
    ''.join(current_path)