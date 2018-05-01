from tkinter import *
import xlrd
import _mysql
import pymysql
import string
import random
from string import digits, ascii_uppercase, ascii_lowercase
from itertools import product

# connection = pymysql.connect(
#     host='10.20.32.107',
#     user='tubes',
#     password='123456789',
#     db='sister'
# )
#
# def database ():
#    with connection.cursor() as cursor:
#       sql = "INSERT INTO `database`(`username`,`password`) VALUES (%s,%s)"
#       try:
#          cursor.execute(sql,(e1.get(),e2.get()))
#       except:
#          print("eror")
#    print("Username = ",e1.get())
#    print("Password = ",e2.get())
#    print("Commit!")
#
# def show_all():
#    with connection.cursor() as cursor:
#       sql = ("SELECT * FROM `database`  ")
#       try:
#          cursor.execute(sql)
#          x = cursor.fetchone()
#          print(x)
#       except:
#          print("ada error")
#



def show_entry_fields():
   x = ("First Name: %s" % (e1.get()))
   return x

master = Tk()
Label(master, text="Masukkan username").grid(row=0)
Label(master, text="Masukkan password").grid(row=1)
Label(master, text="Masukkan password" % show_entry_fields).grid(row=2)



e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Ok', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Show all database', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()