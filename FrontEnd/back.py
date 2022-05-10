import gnupg
from pprint import pprint

def encrypt_data(unencrypted_string):
    gpg = gnupg.GPG()
    encrypted_data = gpg.encrypt(unencrypted_string, '201901026@daiict.ac.in')
    encrypted_string = encrypted_data
    return encrypted_string

def decrypt_data(encrypted_string):
    gpg = gnupg.GPG()
    decrypted_data = gpg.decrypt(str(encrypted_string))
    decrypted_string=str(decrypted_data)
    return decrypted_string


