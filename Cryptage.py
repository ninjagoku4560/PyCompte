from cryptography.fernet import Fernet


def writeKey(path=None):
    # key generation
    key = Fernet.generate_key()

    # string the key in a file
    if path == None:
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
    else:
        with open(path + '/filekey.key', 'wb') as filekey:
            filekey.write(key)


def Encrypt(file,keyfile):
    try:
        # opening the key
        with open(keyfile, 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open(file, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    except FileNotFoundError as e:
        print(f"Error: {e}")


def Decrypt(file,keyfile):
    try:
        # opening the key
        with open(keyfile, 'rb') as filekey:
            key = filekey.read()
        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open(file, 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(file, 'wb') as dec_file:
            dec_file.write(decrypted)
    except FileNotFoundError as e:
        print(f"File Not Found: {e}")
