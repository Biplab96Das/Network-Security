import socket

# Initialize Socket Instance
sock = socket.socket()
print ("Client created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established with the Server.')
# Send a greeting to the server
sock.send('Please send me the file'.encode())

# Write File in binary
file = open('client-file.txt', 'wb')

# Keep receiving data from the server
line = sock.recv(1024)

while(line):
    file.write(line)
    line = sock.recv(1024)

print('File has been received successfully.It contains following:')
file = open("client-file.txt", "r")

print(file.read())
file.close()
sock.close()
print('Connection Closed.')
