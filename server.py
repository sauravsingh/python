import socket
s=socket.socket()
#host=socket.gethostname()
host="10.216.139.68"
port=12345
s.bind((host,port))

s.listen(5)


while True:
    c, addr = s.accept()
    print('Got the connection from', addr)
    c.send(str.encode('Thank you for connection'))

    print(str(c.recv(1024)))

    #c.close()
