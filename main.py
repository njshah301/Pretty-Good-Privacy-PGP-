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
    pwo.set_scope('List')
    pwo.put_markdown(""" # Pretty Good Privacy (PGP)""")
    pwo.put_buttons(['Encryption'], onclick = [front.encrypt])
    pwo.put_buttons(['Decryption'], onclick = [front.decrypt])
    pwo.put_buttons(['List Key'], onclick = [front.list_key])


    while(True):
        pass
    
if __name__ == '__main__':
    home_page()
