import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip="192.168.0.159"
port=4040
s.connect((ip,port))
print("connected..")

while 1:
    recv_msg = s.recv(1024)
    recv_msg = recv_msg.decode()
    print(recv_msg)
    msg=input("Enter your Text : ")
    msg=msg.encode()
    s.send(msg)