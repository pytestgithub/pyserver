import socket
host=socket.gethostbyname(socket.gethostname())
port=9999
client=socket.socket(socket.AF_INET,scoket.SOCK_STREAM)
client.connect((host,port))
