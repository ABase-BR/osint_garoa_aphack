#!/usr/bin/python3

from pywhatcms import whatcms
import sys

if len(sys.argv) >= 3:
    #print(sys.argv[0])
    key = sys.argv[1]
    target = sys.argv[2]

    whatcms(key, target)
    print(whatcms.name)
    print(whatcms.code)
    print(whatcms.confidence)
    print(whatcms.cms_url)
    print(whatcms.version)
    print(whatcms.msg)
    print(whatcms.id)
    print(whatcms.request)
    print(whatcms.request_web)
else:
    print("./whatcms-check.py s3cr3t-k3y-4p1 https://alvo")
