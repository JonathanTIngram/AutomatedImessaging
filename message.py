from py_imessage import imessage
from time import sleep

phone = "##########" #Enter the iphone number you want to message in this string

with open("speech.txt", "r") as f:
    text = f.readlines()

print(text[0])
i = 0

while (i < len(text)):
    guid = imessage.send(phone, text[i])
    resp = imessage.status(guid)
    print(f'Message was read at {resp.get("date_read")}')
    i = i + 1

    
