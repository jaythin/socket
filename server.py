#coding:utf-8
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10002)

server.bind(server_address)

server.listen(10)
print(server)
conn,addr = server.accept()

print(conn)

response = 'ok what do you want?'
response = response.encode('utf-8')

while True:
    if conn:
        data = conn.recv(1024).decode('utf-8')
        print(data)
        conn.send(response)
server.close()
