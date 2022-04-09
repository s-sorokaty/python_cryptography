from cryptography.fernet import Fernet


class Symmetric_encriptor:
    key : str

    def  __init__(self, keypath : str = 'ecriptors/symmetry/crypto.key'):
        if len(keypath) == 0:
            key = Fernet.generate_key()
            with open(keypath + 'crypto.key' , 'wb') as key_file:
                key_file.write(key)
            self.key = open(keypath + 'crypto.key', 'rb').read()
        else: 
            self.key = open(keypath + 'crypto.key', 'rb').read()

    def encrypt(self, filename):
        f = Fernet(self.key)
        with open(filename, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)
        with open('ecriptors/symmetry/examples/encrypt/text.txt', 'wb') as file:
            file.write(encrypted_data)
            pass

    def decrypt(self, filename):
        f = Fernet(self.key)
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open('ecriptors/symmetry/examples/decrypt/text.txt', 'wb') as file:
            file.write(decrypted_data)
            pass