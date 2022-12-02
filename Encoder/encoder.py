from fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("D:/YoCheckMaCode/Encoder/key.key", "wb") as file:
        file.write(key)
    return key


files = []
for file in os.listdir():
    if file == "encoder.py" or file == "decoder.py" or file == "key.key":
        continue
    else:
        if os.path.isfile(file):
            files.append(file)


def encoder():
    key = generate_key()
    for file in files:
        print(file)

encoder()