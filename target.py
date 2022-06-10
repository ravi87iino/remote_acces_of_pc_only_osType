import socket
import time
import sys
import os
import subprocess
my_addre = ("0.0.0.0", 13679)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try :
    s.bind(my_addre)
    print('socket and binding done')
    os_name = sys.platform
    print(os_name)
    data = s.recvfrom(20)
    print(data)  # for checking otherwise not neccessary
    new_name = os_name.encode('ascii')
    s.sendto(new_name, data[1])
except:
    print("error")
