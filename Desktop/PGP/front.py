from turtle import onclick
from main import *
import pywebio.output as pwo
import gnupg
import back

from pywebio.input import textarea
def encrypt():
    pwo.clear()
    main_data=textarea('Enter the text you want to encrypt:', type='text')
    encrypted_data=back.encrypt_data(main_data)
    pwo.clear()
    pwo.put_markdown(""" # Encrypted Key""")
    pwo.put_text(str(encrypted_data))
    pwo.put_buttons(['Home Page'], onclick = [home_page])
def decrypt():
    pwo.clear()
    encrypt_data=textarea('Enter the text you want to decrypt:', type='text')
    decrypted_data=back.decrypt_data(encrypt_data)
    pwo.clear()
    pwo.put_markdown(""" # Decrypted Key""")
    pwo.put_text(decrypted_data)
    pwo.put_buttons(['Home Page'], onclick = [home_page])

def list_key():
    pwo.clear()
    gpg = gnupg.GPG()
    public_keys = gpg.list_keys()
    private_keys = gpg.list_keys(True)
    pwo.put_markdown(""" # Public Key""")
    pwo.put_text(str(public_keys))
    pwo.put_markdown(""" # Private Key""")
    pwo.put_text(str(private_keys))
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
