#Shodan
from shodan import Shodan
import sys

if len(sys.argv) >= 3:
    #print(sys.argv[0])
    key = sys.argv[1]
    target = sys.argv[2]

    def green_shodansearch(name_host,shodan_key):
        # ADD Key config
        api = Shodan(shodan_key)
        host = api.host(name_host)
        # print(ipinfo)
        # Print general info
        print("""
    IP: {}
    Organization: {}
    Operating System: {}
                        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        # Print all banners
        for item in host['data']:
            print("""
    Port: {}
                                """.format(item['port']))

    nome_host = target
    shodan_key = key
    print(green_shodansearch(nome_host,shodan_key))
else:
    print("Algo deu errado!")
