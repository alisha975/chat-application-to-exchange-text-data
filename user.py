import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_ip="192.168.0.159"#your system ip -address
port=4040

s.bind((server_ip,port))
s.listen(1)
conn,addr=s.accept()
print("connected..")

while 1:
    msg=input("Enter your Text : ")
    msg = msg.encode()
    conn.send(msg)
    recv_msg = conn.recv(1024)
    recv_msg = recv_msg.decode()
    print(recv_msg)
