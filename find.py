#!/usr/bin/python3

# code by Craglitch

# IMPORT MODULE

import requests
import os
import sys
import time
# BANNER
input("tap any key to continue except ctrl + c ")
os.system("clear")
os.system("cat banner")

# READ FILE PAGE TXT

page=open('page.txt', 'r')
admin=page.readlines()
page.close()

# VARIABLE LINK
link=input("\033[0;32mserver links :\033[0m ")
os.system("clear")
def getpage() :
    for x in admin :
        ap=x.strip()
        linkpage=link+ap
        check=requests.get(linkpage)
        if check.status_code == 200:
            print("\033[32mpage admin found : "+linkpage)
            break
        elif check.status_code == 404:
            print("\033[31mpage admin not found : "+linkpage)
            continue
        else:
            print("error : something went wrong")
            break
try:
    os.system("clear")
    print("\033[0;34mPLEASE WAIT SCANNING IS START !!! \033[0;32m:\033[0m \""+link+"\"")
    print("\033[0;32m-------------------------------------------------------------------------")
    time.sleep(0.001)
    getpage()
except requests.exceptions.MissingSchema:
    print("\033[31mMissing Schema \033[0m: you forget put https://www.example.com/ or http://www.example.com//")
    sys.exit()
except KeyboardInterrupt:
    print("\033[33mkeyboard interrupt quit")
    sys.exit()
except requests.exceptions.ConnectionError:
    print("\033[0mConnectionError cant requests : "+link)
    print("check link correct or check connection stable")
    sys.exit()
