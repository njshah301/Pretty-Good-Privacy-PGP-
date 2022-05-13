# PGP (Pretty Good Privacy)
## _Implementation procedure:_

We used Kleopatra openPGP software to implement PGP for Email data encryption. By using this software we tried to generate encrypted message to our actual text message. 
PGP encryption uses a combination of symmetric key encryption (a single-use key) and public key encryption.
We tested and got to know how PGP works. After this, we tried to implement this encryption method through web application using python.

Firstly, we made a message as input which we want to send through email with PGP encryption so, we used "gnupg" library to access all PGP functionalities. By using gnupg functionality we encrypt the message using public key. Then, we will decrypt our encrypted file using decryption function of gnupg library. For web development using python we used pywebio library. we build frontend and back end using the same pywebio functionality. 

