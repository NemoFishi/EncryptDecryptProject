from FileKey import *


def decryptor():
    decryptFile = "decrypt.txt"

    # open encrypted file
    with open('encrypt.txt', 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypt file
    decrypted = readKey().decrypt(encrypted)

    # writing the decrypted data
    with open('decrypt.txt', 'wb') as dec_file:
        dec_file.write(decrypted)

    print("Text decrypted and saved to:", decryptFile)
