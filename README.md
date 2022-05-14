# PGP (Pretty Good Privacy)
PGP stands for Pretty Good Privacy.Phil Zimmermann created the first version of PGP encryption in 1991. PGP was designed to provide all four aspects of security.i.e., privacy, integrity, authentication, and non-repudiation in the sending of email. PGP uses a combination of secret key encryption and public key encryption to provide privacy. PGP is an open source and freely available software package for email security.The name, "Pretty Good Privacy" was inspired by the name of a grocery store, "Ralph's Pretty Good Grocery", featured in radio host Garrison Keillor's fictional town, Lake Wobegon. This first version included a symmetric-key algorithm that Zimmermann had designed himself.Zimmermann had been a long-time anti-nuclear activist, and created PGP encryption.

We implemented PGP functionality by using Kleopatra OpenPGP software. 

## _How does PGP encryption works?_
At a basic level, PGP encryption uses a combination of two forms of encryption: symmetric key encryption, and public-key encryption.
The mathematics behind encryption can get pretty complex, so here we’ll stick to the basic concepts. At the highest level, this is how PGP encryption works:

1. PGP generates a random session key using one of two (main) algorithms. This key is a huge number that cannot be guessed, and is only used once.
2. This session key is encrypted. This is done using the public key of the intended recipient of the message. The public key is tied to a particular person’s identity, and anyone can use it to send them a message.
3. The sender sends their encrypted PGP session key to the recipient, and they are able to decrypt it using their private key. Using this session key, the recipient is now able to decrypt the actual message.

Reference : https://www.varonis.com/blog/pgp-encryption#:~:text=Pretty%20Good%20Privacy%20(PGP)%20is,is%20based%20on%20two%20factors

## _Implementation procedure:_

We used Kleopatra openPGP software to implement PGP for Email data encryption. By using this software we tried to generate public key.
Python code to generate the PGP key in the key store :
#Image

This code automatically puts the the PGP key into the key store. The email address is your unique identifier for accessing the key from the key store. As you will see in the examples below, in order to encrypt a file we will use the public key portion from the key store; however, in order to decrypt that same file, we will use the private key portion with the passphrase.
**Encryption:**
Let's find out how to encrypt the content of text file using python and PGP public key portion from the key store:
#Image

The encrypted message is as below:
#image

**Decryption:**
In order to decrypt the contents of this file, we need to use the PGP private key from the key store and the passphrase is needed when using the private key. Here is the Python code for that:
#image

After this, we tried to implement this encryption method through web application using python.

For web application we used pywebio library which gave us verious functionalities for frontend and backend.
we build encryption and decryption functions in the backend which are called using buttons given in the frontend.


