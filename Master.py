import os
import mysql.connector as PyMySql
import time
import pickle
import OAuth
import DB
import Setup
print('''Welcome to Library Management System
    Please enter your credentials to continue:''')
start = open("setup.txt","r+")
if (start != 1):
    print("Wecome to the setup")
    Setup.initiate()
    OAuth.admin()
    start.write(1)
start.close()
OAuth.log()

con = pymysql.connect(host = 'localhost' ,user = 'root' ,passwd = 'sql' ,database = 'Library')
cursor = con.cursor()
