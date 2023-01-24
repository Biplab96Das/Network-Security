from cryptography.fernet import Fernet


f=open("server-file.txt",'r')
message = f.read()


key = Fernet.generate_key()



fernet = Fernet(key)


encMessage = fernet.encrypt(message.encode())

with open("client-file.txt", 'wb') as f:
    f.write(encMessage)



print("original message:\n",message)

decMessage = fernet.decrypt(encMessage).decode()
with open("decrypted-file.txt", 'w') as f:
    f.write(decMessage)
