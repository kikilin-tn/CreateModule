#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import getpass
import os

_username = 'Kiki Lin'
_password = '12345'

username = input("請輸入用戶名稱:\n")
password = getpass.getpass("請輸入密碼:\n") #使用者輸入時不會出現字

if _username == username and _password == password:
    #print("Weclome %s Login " % username)
    print("Weclome! " + username)
else:
    print("invalid username or password\n")

os.system('pause')

#print(username, password)
