import gnupg
from pprint import pprint

def encrypt_data(unencrypted_string):
    gpg = gnupg.GPG()
    #unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = gpg.encrypt(unencrypted_string, '201901026@daiict.ac.in')
    encrypted_string = str(encrypted_data)
    return encrypted_string