import threading
import time
import pymysql
import zmq
from Unsyncgnizedinteger import UnsynchronizedInteger

number = UnsynchronizedInteger()
connection = pymysql.connect(
    host="192.168.0.103",
    user="tubes",
    password='123456789',
    db='sister'
)


class myThread1(threading.Thread):
    def __init__(self, threadID, so):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.PUSH)
        self.so = so

    def run(self):
        self.sock.bind("tcp://192.168.0.113:5555")

        with connection.cursor() as cursor:
            sql = ("SELECT * FROM `database`  ")
            try:
                cursor.execute(sql)
                x = cursor.fetchall()
            except:
                print('ada eror')
        i = 0
        # if end = true:
        #        while i<len(x) and self.bool.get==1:
        print("ini balikan")
        print(self.so.get())
        while i < len(x) and self.so.get() == 1:
            ##        while i<len(id):
            print(self.so.getcounter())
            time.sleep(1)
            ids, now = x[i]
            pesan = "{username},{passw}".format(username=ids, passw=now)

            self.sock.send(pesan.encode())
            print("sent: \n pesan :{psn}".format(psn=pesan))
            i += 1
        print("selesai kirim")
        print(self.so.getcounter())
        while self.so.getcounter() >= 0:
            #        while True:
            pesan = "selesai"
            self.sock.send(pesan.encode())
            self.so.setcounter(-1)
        print("selesai ini")
        self.sock.close()


class myThread2(threading.Thread):
    def __init__(self, threadID, so):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.context = zmq.Context()
        self.sock1 = self.context.socket(zmq.PULL)
        self.so = so

    def run(self):
        self.sock1.bind("tcp://192.168.0.113:5005")
        menerima = 1
        while menerima == 1:
            message = str(self.sock1.recv().decode("utf-8"))
            if message == "connect":
                self.so.setcounter(1)
                print(self.so.getcounter())
                print(message)
            elif message == "sukses":
                self.so.set(0)
                self.so.setcounter(-1)
                menerima = 0
                print(message)
                self.sock1.close()


thread1 = myThread1(1, number)
thread2 = myThread2(2, number)
#
thread1.start()
thread2.start()
#
#
print("Exiting Main Thread")