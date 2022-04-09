from ecriptors.symmetry.symmetry_module import Symmetric_encriptor 
from ecriptors.asymmetry.asymmetry_module import Asymmetric_encriptor


expample_filename = 'ecriptors/symmetry/examples/text.txt'
encrypt_filename = 'ecriptors/symmetry/examples/encrypt/text.txt'
sum_key = 'ecriptors/symmetry/'

Symmetric_encriptor = Symmetric_encriptor(sum_key)

Symmetric_encriptor.encrypt(expample_filename)
Symmetric_encriptor.decrypt(encrypt_filename)

expample_filepath = 'ecriptors/asymmetry/examples/'
asum_key = 'ecriptors/asymmetry/'


Asymmetric_encriptor = Asymmetric_encriptor(asum_key)

Asymmetric_encriptor.encrypt(expample_filepath)
Asymmetric_encriptor.decrypt(expample_filepath)

