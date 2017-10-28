import socket
import os

fileName = 'talk'
sock = socket.socket(family=socket.AF_UNIX)
bound = False
try:
    sock.bind(fileName)
    bound = True
    sock.listen()
    # The initial socket is used to listen for acceptions. The new
    # socket, dataSock, is used for communication.
    # Connection need happen just once for repeated communication.
    dataSock, dataSockAddress = sock.accept()
    #thing = bytearray()
    #sock.recvmsg(4096)
    while True:
        data = dataSock.recv(2**3)
        if not data:
            break
        print(data)
    dataSock.close()
    sock.close()
except OSError as e:
    # Address already in use
    if 98 == e.errno:
        sock.connect(fileName)
        while True:
            msg = input("Write something: ")
            if 'quit' == msg:
                break
            sock.send(msg.encode())
    else:
        raise e
finally:
    if bound:
        os.remove(fileName)
