import gnupg
from pprint import pprint

gpg = gnupg.GPG()
unencrypted_string = 'Who are you? How did you get in my house?'
encrypted_data = gpg.encrypt(unencrypted_string, '201901026@daiict.ac.in')
encrypted_string = str(encrypted_data)
decrypted_data = gpg.decrypt(encrypted_string, passphrase='my passphrase')
decrypted_string=str(decrypted_data)
print (decrypted_string)

