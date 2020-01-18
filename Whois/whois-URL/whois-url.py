import requests

import sys

if len(sys.argv) >= 2:
    #print(sys.argv[0])
    dominio = sys.argv[1]
    r = requests.get('https://api.hackertarget.com/whois/?q='+dominio)

    #print(r.status_code)
    print(r.text)
    #print(r.headers['content-type'])
else:
    print("algo deu errado")
