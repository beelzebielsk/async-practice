import socket
import os

fileName = 'talk'
sock = socket.socket(family=socket.AF_UNIX)
bound = False
try:
    sock.bind(fileName)
    bound = True
    sock.listen()
    dataSock, dataSockAddress = sock.accept()
    #thing = bytearray()
    #sock.recvmsg(4096)
    while True:
        data = dataSock.recv(2**3)
        if not data:
            break
        print(data)
        dataSock.send(b'ack')
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
            data = sock.recv(2**3)
            print(data)
    else:
        raise e
finally:
    if bound:
        os.remove(fileName)
