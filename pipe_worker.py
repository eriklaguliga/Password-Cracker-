import zmq
from tkinter import *

context = zmq.Context()
sock1 = context.socket(zmq.PULL)
sock1.connect("tcp://192.168.0.113:5555")
sock2= context.socket(zmq.PUSH)
sock2.connect("tcp://192.168.0.113:5005")


sock2.send("connect".encode())
x=False
while x==False:
    message = str(sock1.recv().decode("utf-8"))
    print("asdf")
    if message!= "selesai":
        username,password= message.split(",")
        print("Username = "+username+"\nPassword = "+password)
        if username=="rock426" and password=="sitge":
            sock2.send("sukses".encode())
            print("ini sudah succes")
            x=True
    else:
        x = True
print("selesai")