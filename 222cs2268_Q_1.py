#In order to work with Crypto module run:"pip install pycryptodome"
#if pip is not already installed then do the following:
#run this three before installing:1)"sudo apt-get update" 2)"sudo apt-get upgrade" 3)"sudo apt install python3-pip"
#Now open terminal and run the Rsa message Encryption program "222cs2268_Q_1.py" using "python3 222cs2268_Q_1.py" write your message and boom!Magic.
#Author : Biplab Das. Roll No : 222CS2268. DEPT.:CSE(IS)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
msg = input("Insert the message here: ")
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode())
print("Encrypted: ", binascii.hexlify(encrypted))
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted: ', decrypted.decode())
