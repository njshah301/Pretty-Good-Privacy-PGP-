# PGP (Pretty Good Privacy)
PGP stands for Pretty Good Privacy.Phil Zimmermann created the first version of PGP encryption in 1991. PGP was designed to provide all four aspects of security.i.e., privacy, integrity, authentication, and non-repudiation in the sending of email. PGP uses a combination of secret key encryption and public key encryption to provide privacy. PGP is an open source and freely available software package for email security.The name, "Pretty Good Privacy" was inspired by the name of a grocery store, "Ralph's Pretty Good Grocery", featured in radio host Garrison Keillor's fictional town, Lake Wobegon. This first version included a symmetric-key algorithm that Zimmermann had designed himself.Zimmermann had been a long-time anti-nuclear activist, and created PGP encryption.

We implemented PGP functionality by using Kleopatra OpenPGP software. 

## _How does PGP encryption works?_
At a basic level, PGP encryption uses a combination of two forms of encryption: symmetric key encryption, and public-key encryption.
The mathematics behind encryption can get pretty complex, so here we’ll stick to the basic concepts. At the highest level, this is how PGP encryption works:

1. PGP generates a random session key using one of two (main) algorithms. This key is a huge number that cannot be guessed, and is only used once.
2. This session key is encrypted. This is done using the public key of the intended recipient of the message. The public key is tied to a particular person’s identity, and anyone can use it to send them a message.
3. The sender sends their encrypted PGP session key to the recipient, and they are able to decrypt it using their private key. Using this session key, the recipient is now able to decrypt the actual message.


## _Implementation procedure:_

We used Kleopatra openPGP software to implement PGP for Email data encryption. By using this software we tried to generate public key and certificates.

![certificates_details](https://user-images.githubusercontent.com/58663029/168425231-953edcdd-ad24-4372-9ebe-ae9abc56e68b.png)

The email address is your unique identifier for accessing the key from the key store. As you will see in the examples below, in order to encrypt a file we will use the public key portion from the key store; however, in order to decrypt that same file, we will use the private key portion with the passphrase.

Below will be the Homepage of our Application:

![homepage](https://user-images.githubusercontent.com/58663029/168425277-1c6d8a9a-fa55-43d9-bc5a-9733e6c7f0e7.png)

**Encryption:**

We can do two types of Encryption here:

# 1. Add a secret file
# 2. Add a secret message
![Encryption_Page](https://user-images.githubusercontent.com/58663029/168425314-29347b76-6699-47df-b358-50ccf279281f.png)

# 1. Add a secret file
![secret_file](https://user-images.githubusercontent.com/58663029/168425415-7e8dff14-7c58-48db-80fa-d59a2e1a29e3.png)

The encrypted message is as below:
![encryted key](https://user-images.githubusercontent.com/58663029/168425429-37989d73-b3d6-4fbb-8802-2c4c81bdc759.png)


**Decryption:**
In order to decrypt the contents of this file, we need to use the PGP private key from the key store and the passphrase is needed when using the private key. Here is 
![decrypted_key](https://user-images.githubusercontent.com/58663029/168425503-b6c9cee0-09e7-43da-940b-f32975725f83.png)


# 2. Add a secret message
![message](https://user-images.githubusercontent.com/58663029/168425796-75f1f4d0-786e-4f59-9d59-cc5e2e1f95ff.png)

The encrypted message is as below:


![enct2](https://user-images.githubusercontent.com/58663029/168425547-b7765f69-df0e-484b-b5b5-e5697659f6fd.png)


**Decryption:**
In order to decrypt the contents of this file, we need to use the PGP private key from the key store and the passphrase is needed when using the private key. Here is 

![dec2](https://user-images.githubusercontent.com/58663029/168425832-34f4d5e8-8ae0-4195-9a68-c724b361401b.png)

## Cloud Deployment

I have made and Azure App Service for python to deploy my application in production. The application needs to deploy on cloud because it can be continuously integreted and scaled as per our use cases.


![azure](https://user-images.githubusercontent.com/58663029/168425722-fea438c9-f0b3-4e63-82ce-36012c99811d.png)


# References


https://www.varonis.com/blog/pgp-encryption#:~:text=Pretty%20Good%20Privacy%20(PGP)%20is,is%20based%20on%20two%20factors


