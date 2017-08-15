import socket

s=socket.socket()
#host=socket.gethostname()
host="10.216.139.68"
port=12345

s.connect((host,port))

print(str(s.recv(1024)))
msg = input("Enter your name: ")

s.send(str.encode(msg))

s.close()
