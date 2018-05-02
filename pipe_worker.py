import zmq
from tkinter import *

context = zmq.Context()
sock1 = context.socket(zmq.PULL)
sock1.connect("tcp://192.168.43.5:5555")
sock2= context.socket(zmq.PUSH)
sock2.connect("tcp://192.168.43.5:5005")


sock2.send("connect".encode())
def crack():
    x=False
    while x==False:
        message = str(sock1.recv().decode("utf-8"))
        print("asdf")
        if message!= "selesai":
            username,password= message.split(",")
            print("Username = "+username+"\nPassword = "+password)
            if username==e1.get() and password==e2.get():
                sock2.send("sukses".encode())
                print("ini sudah succes")
                x=True
        else:
            x = True
print("selesai")

master = Tk()
Label(master, text="Masukkan username").grid(row=0)
Label(master, text="Masukkan password").grid(row=1)




e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Ok', command=crack).grid(row=3, column=1, sticky=W, pady=4)


mainloop()