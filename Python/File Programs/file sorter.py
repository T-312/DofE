import os
import shutil
import time

username = os.getlogin()
a = f"/Users/{username}/Downloads/"
os.chdir(r"C:/")
username = os.getlogin()

print("Started")
while True:
    for f in os.listdir(a):
        file_name, file_ext = (os.path.splitext(f))


        main = f'C:/Users/{username}/Downloads/'
        source = main + f

        if file_ext == ".txt" or file_ext == '.doc' or file_ext == ".docx" or file_ext == ".DOC" or file_ext == ".DOCX":
            destination = 'C:/Users/Tim/Docs/'
            dest = shutil.move(source, destination)

        elif file_ext == ".pptx" or file_ext == ".PPTX" or file_ext == ".ppt" or file_ext == ".PPT":
            destination = 'C:/Users/Tim/Powerpoint/'
            dest = shutil.move(source, destination)

        elif file_ext == '.exe' or file_ext == ".EXE":
            destination = 'C:/Users/Tim/Apps/'
            dest = shutil.move(source, destination)

        elif file_ext == '.pdf' or file_ext == ".PDF":
            destination = 'C:/Users/Tim/pdf/'
            dest = shutil.move(source, destination)

        elif file_ext == ".JPG" or file_ext == ".jpg" or file_ext == ".JPEG" or file_ext == ".jpeg" or file_ext == ".img" or file_ext == ".IMG" or file_ext == ".PNG" or file_ext == ".png":
            destination = 'C:/Users/Tim/pics/'
            dest = shutil.move(source, destination)

        elif file_ext == ".ICO" or file_ext == ".ico":
            destination = 'C:/Icons/'
            dest = shutil.move(source, destination)

        elif file_ext == ".mp4" or file_ext == ".MP4":
            destination = 'C:/Users/Tim/Videos/'
            dest = shutil.move(source, destination)

        elif file_ext == ".xlsx" or file_ext == ".XLSX":
            destination = 'C:/Users/Tim/Excel/'
            dest = shutil.move(source, destination)

        elif file_ext == ".mp3" or file_ext == ".MP3":
            destination = 'C:/Users/Tim/Music/'
            dest = shutil.move(source, destination)