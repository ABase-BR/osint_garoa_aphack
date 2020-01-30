import yandex_search
import sys

if len(sys.argv) >= 2:
    #print(sys.argv[0])
    site = sys.argv[1]
    yandex = yandex_search.Yandex(api_user='my-user', api_key='mykey')
    print(yandex.search('site:'+site).items)
else:
    print("algo deu errado")
