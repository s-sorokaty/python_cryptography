import hashlib

from ecriptors.symmetry.symmetry_module import Symmetric_encriptor 
from ecriptors.asymmetry.asymmetry_module import Asymmetric_encriptor
import glob

for wwid in glob.glob("/sys/block/*/device/wwid"):
    print(wwid)
    with open(wwid, "r") as file:
        try:
            data = file.readline().strip()
            print(data)
        except:
            print("not readable")


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
password = 'WASD1234'


class RunCountError(Exception):
    pass


with open('run_count.txt') as f:
    run_count = int(f.read())
with open('run_count.txt', 'w') as f:
    f.write(str(run_count + 1))


if __name__ == '__main__':
    if run_count > 5:
        raise RunCountError
    user_password = ''
    while user_password != password:
        print('password:')
        user_password = input()
    print('you are logined')

    while True:
        pass

