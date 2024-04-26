from cryptography.fernet import Fernet


def createKey():
    # generate key
    key = Fernet.generate_key()

    # write key to file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)


def readKey():
    # read key file
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # assign key to variable
    fernet = Fernet(key)

    return fernet
