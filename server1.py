import socket


host=socket.gethostbyname(socket.gethostname())
port=9999
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind((host,port))
print("socket server started")
s.listen(10)
print('# Socket now listening')

# Wait for client
print("waiting for client")
conn, addr = ser.accept()

print('# Connected to ' + addr[0] + ':' + str(addr[1]))

# Receive data from client    
data = conn.recv(1024)
line = data.decode('UTF-8')    # convert to string (Python 3 only)
line = line.replace("\n","")   # remove newline character
print( line )     

ser.close()
