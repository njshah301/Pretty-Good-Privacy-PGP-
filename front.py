from turtle import onclick
from main import *
import pywebio.output as pwo
import gnupg
import pandas as pd
import back
import pywebio.input as pwi
from pywebio.input import textarea

def call():
        pwo.put_html('''<!DOCTYPE html>
    <html>
    <head>
    <style>
    body {

    }
    </style>
    </head>
    <body>
        <span style="position: absolute;left:80%;top:90%;font-style:bolder;color: green+black+blue ;border:2px solid black;"> Developed by ❤ Nilay Shah
    <a href="https://www.facebook.com/nilay.shah.92775" >

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/js/all.min.js"></script>

    <a href="https://www.facebook.com/nilay.shah.92775"><i class="fab fa-facebook-square"></i></a>
    &nbsp;


    <a href="https://www.instagram.com/nilay_shah_nj/" >

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    
    <i class="fab fa-instagram"></i></a>&nbsp;
    <a href="https://github.com/njshah301" >
        
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://kit.fontawesome.com/a076d05399.js"></script>
        
        <i class="fab fa-github"></i>
    
    </a>
    </span>  
    </body>
    </html>
    ''' )

def encrypt_file():
    pwo.clear()
    call()
    userfile=pwi.file_upload('Choose your file')
    open(userfile['filename'],'wb').write(userfile['content'])
    df=pd.read_csv(userfile['filename'])
    main_data=df.to_string(index=False)
    encrypted_data=back.encrypt_data(main_data)
    pwo.clear()
    call()
    pwo.put_markdown(""" # Encrypted Key""")
    pwo.put_text(str(encrypted_data))
    pwo.put_buttons(['Home Page'], onclick = [home_page])
def encrypt_message():
    pwo.clear()
    call()
    main_data=textarea('Enter the text you want to encrypt:', type='text')
    encrypted_data=back.encrypt_data(main_data)
    pwo.clear()
    call()
    pwo.put_markdown(""" # Encrypted Key""")
    pwo.put_text(str(encrypted_data))
    pwo.put_buttons(['Home Page'], onclick = [home_page])

def encrypt():
    pwo.clear()
    call()
    pwo.put_markdown(""" # Enter a secret file""")
    pwo.put_buttons(['Add file'], onclick = [encrypt_file])
    pwo.put_markdown(""" # Enter a secret message""")
    pwo.put_buttons(['Add message'], onclick = [encrypt_message])
    
def decrypt():
    pwo.clear()
    call()
    encrypt_data=textarea('Enter the text you want to decrypt:', type='text')
    decrypted_data=back.decrypt_data(encrypt_data)
    pwo.clear()
    pwo.put_markdown(""" # Decrypted Key""")
    pwo.put_text(decrypted_data)
    pwo.put_buttons(['Home Page'], onclick = [home_page])

def list_key():
    pwo.clear()
    call()
    gpg = gnupg.GPG()
    public_keys = gpg.list_keys()
    private_keys = gpg.list_keys(True)
    pwo.put_markdown(""" # Public Key""")
    pwo.put_text(str(public_keys))
    pwo.put_markdown(""" # Private Key""")
    pwo.put_text(str(private_keys))
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
