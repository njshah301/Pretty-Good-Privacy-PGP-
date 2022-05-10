import gnupg
from pprint import pprint

gpg = gnupg.GPG()
public_key_data = open('C:/Users/91997/Desktop/PGP/Nilay Shah_0x91F3A894_public.asc').read()
private_key_data = open('C:/Users/91997/Desktop/PGP/private.asc').read()
public_import_result = gpg.import_keys(public_key_data)
private_import_result = gpg.import_keys(private_key_data)
pprint(public_import_result.results)
pprint(private_import_result.results)



