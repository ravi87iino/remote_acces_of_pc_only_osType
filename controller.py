import socket
import time
import sys
import os
import subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("localhost",13679)
user = input('Enter your name : ')
#os.system('clear')
print("welcome user",user)
print("checking target os")
wait_os = "name of your os ? "
s.sendto(wait_os.encode('ascii'),address)
result_os= s.recvfrom(10)
print(result_os)

