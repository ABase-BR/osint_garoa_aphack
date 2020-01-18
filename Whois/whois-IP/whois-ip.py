import requests

import sys

if len(sys.argv) >= 2:
    #print(sys.argv[0])
    ip = sys.argv[1]
    r = requests.get('https://api.hackertarget.com/whois/?q='+ip)

    #print(r.status_code)
    print(r.text)greenmind/whois:ip
    #print(r.headers['content-type'])
else:
    print("algo deu errado")
