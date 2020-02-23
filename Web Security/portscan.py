import socket
remoteserver = input("enter the port to be scanned")
for port in range(1,8081):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((remoteserver,port))
    if result == 0:
        print("port{}:open".format(port))
    else:
        print("port{}:closed".format(port))
        sock.close()