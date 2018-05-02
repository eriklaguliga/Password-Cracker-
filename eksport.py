import xlrd
import math
import xlrd
import _mysql
import pymysql
import string
import random
from string import digits, ascii_uppercase, ascii_lowercase
from itertools import product

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456789',
    db='sister'
)

file = xlrd.open_workbook("wew.xlsx")
data = file.sheet_by_index(0)

def genap (a):
    if a%2 == 0:
        return True
    else:
        return False


a= []
g = []
g1 = []
for i in range(data.nrows):
    a.append(data.cell_value(i,0))
count = 0
while count<  len(a):

  with connection.cursor() as cursor:
    sql = "INSERT INTO `database`(`username`,`password`) VALUES (%s,%s)"
    try:
        cursor.execute(sql, (a[count],a[count+1]))
    except:
        print('ada eror')
    connection.commit()
    count = count + 2
    print("username",count)

# c = 0
# for i in range(len(a)):
#     c = c +1
#     with connection.cursor() as cursor:
#         if genap(c) == True:
#             sql = "INSERT INTO `database`(`password`) VALUES (%s)"
#             try:
#                 cursor.execute(sql,(a[i]))
#             except:
#                 print('ada eror')
#     connection.commit()
#     print("password=",c)



