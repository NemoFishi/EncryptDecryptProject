from readPDF import *
from Encrypt import *
from Decrypt import *

if __name__ == '__main__':
    fileName = input("What file are you encrypting?: ")

    readPDFStuff(fileName)
    createKey()
    encryptor()
    decryptor()
