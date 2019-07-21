import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_address = ('localhost',10002)
message = 'hello server!'
message = message.encode('utf-8')

print(client)
client.connect(client_address)
client.send(message)

while True:
    data = client.recv(1024)
    print(data)

client.close()
