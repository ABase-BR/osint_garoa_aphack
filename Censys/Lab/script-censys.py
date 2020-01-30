import censys.ipv4
import pprint

import sys

if len(sys.argv) >= 2:
    alvo = sys.argv[1]

    c = censys.ipv4.CensysIPv4(api_id="API ID", api_secret="Secret")

    pp = pprint.PrettyPrinter(indent=4)

    # the report method constructs a report using a query, an aggretaion field, and the
    # number of buckets to bin
    c.report(""" "welcome to" AND tags.raw: "http" """, field="80.http.get.headers.server.raw", buckets=5)

    # the view method lets you see the full JSON for an IP address
    pp.pprint(c.view(alvo))
else:
    print("Não foi passado argumento")
