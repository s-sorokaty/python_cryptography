import hashlib

from ecriptors.symmetry.symmetry_module import Symmetric_encriptor 
from ecriptors.asymmetry.asymmetry_module import Asymmetric_encriptor


expample_filename = 'ecriptors/symmetry/examples/text.txt'
encrypt_filename = 'ecriptors/symmetry/examples/encrypt/text.txt'
sum_key = 'ecriptors/symmetry/'

Symmetric_encriptor = Symmetric_encriptor(sum_key)

with open(encrypt_filename, 'rb') as f:
    a = hashlib.sha256(f.read())
    print(a.digest())

with open(expample_filename, 'rb') as f:
    a = hashlib.sha256(f.read())
    print(a.digest())

# Symmetric_encriptor.encrypt(expample_filename)
# Symmetric_encriptor.decrypt(encrypt_filename)

expample_filepath = 'ecriptors/asymmetry/examples/'
asum_key = 'ecriptors/asymmetry/'


Asymmetric_encriptor = Asymmetric_encriptor(asum_key)

with open(expample_filepath + 'decrypt/text.txt', 'rb') as f:
    a = hashlib.sha256(f.read())
    print(a.digest())


with open(expample_filepath + 'encrypt/text.txt', 'rb') as f:
    a = hashlib.sha256(f.read())
    print(a.digest())


Asymmetric_encriptor.encrypt(expample_filepath)
Asymmetric_encriptor.decrypt(expample_filepath)
Asymmetric_encriptor.check_sign(expample_filepath)



# with open(expample_filepath + 'decrypt/text.txt', 'w') as f:
#     f.write("[b'My secret id']")

Asymmetric_encriptor.encrypt(expample_filepath)

# with open(expample_filepath + 'encrypt/text.txt', 'wb') as f:
#     f.close()

# with open(expample_filepath + 'encrypt/text.txt', 'rb') as f:
#     print(f.read())
Asymmetric_encriptor.check_sign(expample_filepath)
