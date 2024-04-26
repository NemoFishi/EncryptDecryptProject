from FileKey import *
import os


def encryptor():
    encryptionFile = "encrypt.txt"

    # read original text file
    with open('pdfExtraction.txt', 'rb') as file:
        original = file.read()

    # encrypt file
    encrypted = readKey().encrypt(original)

    # write encrypted text
    with open('encrypt.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    with open('encrypt.txt', 'rb') as enc_file:
        encrypted = enc_file.read()

    os.remove("pdfExtraction.txt")
    print("Encrypted as: ", encrypted)
    print("Text encrypted and saved to:", encryptionFile)
