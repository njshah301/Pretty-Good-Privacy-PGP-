def home_page():
    import front
    import back
    import gnupg
    import pywebio.output as pwo
    from pywebio.input import input
    pwo.clear() 
    pwo.put_html('''<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1528&q=80');
}

}
</style>
</head>
<body>
</body>
</html>
''' )
    pwo.set_scope('List')
    pwo.put_markdown(""" # Pretty Good Privacy (PGP)""")
    pwo.put_buttons(['Encryption'], onclick = [front.encrypt])
    pwo.put_buttons(['Decryption'], onclick = [front.decrypt])
    pwo.put_buttons(['List Key'], onclick = [front.list_key])


    while(True):
        pass
    
if __name__ == '__main__':
    home_page()
