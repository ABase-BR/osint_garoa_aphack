#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) >= 2:
    #print(sys.argv[0])
    target = sys.argv[1]
else:
    print("./script-whatcms.py https://globo.com")

rec_site = requests.get('http://sharingmyip.com/?site='+target)

soup = BeautifulSoup(rec_site.text,'html.parser')

qt_textarea = len(soup('textarea'))
msg_list = ['Site (s) neste endereço','DNS para ','Entradas de DNS relacionadas para']

for i in range(qt_textarea):
    if (i == 0):
        print(msg_list[0]+" ")
        print(soup('textarea')[i].string)
    elif i == 1:
        print(msg_list[1]+" ")
        print(soup('textarea')[i].string)
    elif i == 2:
        print(msg_list[2]+" ")
        print(soup('textarea')[i].string)
    else:
        print("Aconteceu algo errado :D")
