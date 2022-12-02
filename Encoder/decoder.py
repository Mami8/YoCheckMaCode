from fernet import Fernet


def get_key():
    key = open("D:/YoCheckMaCode/Encoder/key.txt", "rb").read()
    return key

data = open("D:/YoCheckMaCode/Encoder/file1.txt", "rb").read()

def decode():
    key = get_key()
    decoded = Fernet(key).decrypt(data)
    with open("D:/YoCheckMaCode/Encoder/file1.txt", "wb") as f:
        f.write(decoded)


if input() == "anen ğ":
    decode()


print("You're safe.")
