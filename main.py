def home_page():
    import front
    import back
    import gnupg
    import pywebio.output as pwo
    from pywebio.input import input
    pwo.clear() 
    ig=open("1.jpg",'rb').read()
    pwo.put_image(ig)
    pwo.set_scope('List')
    pwo.put_markdown(""" # Pretty Good Privacy (PGP)""")
    pwo.put_buttons(['Encryption'], onclick = [front.encrypt])
    pwo.put_buttons(['Decryption'], onclick = [front.decrypt])
    pwo.put_buttons(['List Key'], onclick = [front.list_key])


    while(True):
        pass
    
if __name__ == '__main__':
    home_page()
