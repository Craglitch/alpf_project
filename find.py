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
print("\033[0;34mPLEASE WAIT SCANNING IS START !!! \033[0;32m:\033[0m \""+link+"\"")
print(" ")
print(" ")
time.sleep(0.100)
try:
    getpage()
except requests.exceptions.MissingSchema:
    sys.exit()
except KeyboardInterrupt:
    print("keyboard interrupt quit")
    sys.exit()

