import socket

# Initialize Socket Instance
sock = socket.socket()
print ("Client created successfully.")

# Defining port and host
port = 8800
host = '127.0.0.1'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established with the Server.')
# Send a greeting to the server
sock.send('Please send me the file'.encode())



print('File has been received successfully.It contains following encrypted message :\n')
f = open("client-file.txt",'rb')
s = f.read()
print(s)
print("\n")

f = open("decrypted-file.txt",'r')
s = f.read()
print("Decrypted message:")
print(s)
print("\n")
sock.close()
print('Connection Closed.')
