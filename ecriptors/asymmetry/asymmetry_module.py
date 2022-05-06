from cryptography import exceptions
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class Asymmetric_encriptor:
    private_key: rsa.RSAPrivateKey
    public_key: rsa.RSAPrivateKey
    sign = ''

    def __init__(self, keypath: str) -> None:
        # private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
        )
        public_key = private_key.public_key()

        self.private_key = private_key
        self.public_key = public_key

        serial_private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(keypath + 'private.pem', 'wb') as f: f.write(serial_private)
        
        # public key
        serial_pub = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(keypath + 'public.pem', 'wb') as f: f.write(serial_pub)


# make sure the following are imported
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization
#########      Private device only    ##########             
    def __read_private(self, keypath):
        with open(keypath + 'private.pem', "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
    # ######### Public (shared) device only ##########
    def __read_public (self, keypath):
        with open(keypath + 'public.pem', "rb") as key_file:
            return serialization.load_pem_public_key(
                key_file.read(),
            )
    
#     # make sure the following are imported

# ######### Public (shared) device only #########

    def encrypt(self, filepath):
        data = '' 
        with open (filepath + 'text.txt') as f: 
            data = f.read()
        data = data.encode('utf-8')
        data = data.split()
        open(filepath + 'encrypt/text.txt', "wb").close() # clear file
        for encode in data:
            encrypted =  self.public_key.encrypt(
                encode,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            print(encrypted)
            with open(filepath + 'encrypt/text.txt', "ab") as f: f.write(encrypted)
           
    def check_sign(self, filepath):
        with open(filepath + 'encrypt/text.txt', "rb") as f:
            try:
                self.public_key.verify(
                self.sign,
                f.read(),
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256())
            except exceptions.InvalidSignature:
                print("A bad signature failed")
            else:
                print("Good signature verified")


    def decrypt(self, filepath):
        read_data = []
        with open(filepath + 'encrypt/text.txt', "rb") as f:
            self.sign = self.private_key.sign(f.read(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
            
            for encrypted in f:
                read_data.append(
                    self.private_key.decrypt(
                        encrypted,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )))
        with open(filepath + 'decrypt/text.txt', "w") as f: 
            
            f.write(str(read_data))


# # make sure the following are imported
# # from cryptography.hazmat.primitives import hashes
# # from cryptography.hazmat.primitives.asymmetric import padding
# #########      Private device only    ##########

# >>> 