## O que é
Com o **nslookup** conseguimos obter informações sobre registros de DNS de um determinado domínio, host ou IP.

Além disso caso um determinado domínio esteja usando um load balance conseguimos obter informações de quais endereços IPS ele esteja usando.  

## Site

### ultratools
Podemos usar o **ultratools** para obter informações, dessa forma não precisamos usar uma ferramenta para obter informações e sim o site.
```sh
https://www.ultratools.com/tools/dnsLookupResult
```

### hackertarget
Outra solução que podemos usar é o **hackertarget**, além de usar via web podemos usar ela via **API**.
```sh
https://hackertarget.com/dns-lookup/
```

#### hackertarget + API (shellscript)
Podemos usar o shellscript para criar um script para automatizar a pesquisa, vamos usar o curl para a consulta.
```sh
curl https://api.hackertarget.com/dnslookup/?q=businesscorp.com.br
```

Podemos ver o resultado da pesquisa
```sh
businesscorp.com.br.	3599	IN	SOA	ns1.businesscorp.com.br. hostmaster.businesscorp.com.br. 2019030507 3600 900 604800 1
businesscorp.com.br.	3599	IN	MX	10 mail.businesscorp.com.br.
businesscorp.com.br.	3599	IN	NS	ns2.businesscorp.com.br.
businesscorp.com.br.	3599	IN	NS	ns1.businesscorp.com.br.
businesscorp.com.br.	3599	IN	A	37.59.174.225
businesscorp.com.br.	3599	IN	HINFO	"SERVIDOR DELL" "DEBIAN - key:0989201883299"
businesscorp.com.br.	3599	IN	TXT	"v=spf1 include:key-9283947588214 ?all"
```

Para melhorar podemos usar argumentos, assim podemos passar o valor do site via argumento.
```sh
#!/bin/bash

# check arg
if [[ "$1" == "" ]]
then
  echo "Não foi passado nenhum argumento"
else
  ALVO="$1"
  curl https://api.hackertarget.com/dnslookup/?q=$ALVO
fi
```

#### hackertarget API + shellscript + docker
Podemos ainda criar um container docker para ter todos os pré requisitos e esse exemplo a imagem tem menos de 10 mb.

Vamos usar o script anterior e colocar o nome dele de **dnslookup.sh**.
```sh
#!/bin/bash

# check arg
if [[ "$1" == "" ]]
then
  echo "Não foi passado nenhum argumento"
else
  ALVO="$1"
  curl https://api.hackertarget.com/dnslookup/?q=$ALVO
fi
```

Depois vamos criar um Dockerfile
```sh
FROM alpine:3.10

RUN apk add --no-cache curl

WORKDIR /root

ADD . .

RUN chmod +x dnslookup.sh.sh

ENTRYPOINT ["sh","/root/dnslookup.sh.sh"]
```

Usar a imagem
```sh
sudo docker run -it --rm "greenmind/hackertarget:dnslookup" businesscorp.com.br
```

O resultado vai ser
```sh
businesscorp.com.br.	3599	IN	SOA	ns1.businesscorp.com.br. hostmaster.businesscorp.com.br. 2019030507 3600 900 604800 1
businesscorp.com.br.	3599	IN	MX	10 mail.businesscorp.com.br.
businesscorp.com.br.	3599	IN	NS	ns2.businesscorp.com.br.
businesscorp.com.br.	3599	IN	NS	ns1.businesscorp.com.br.
businesscorp.com.br.	3599	IN	A	37.59.174.225
businesscorp.com.br.	3599	IN	HINFO	"SERVIDOR DELL" "DEBIAN - key:0989201883299"
businesscorp.com.br.	3599	IN	TXT	"v=spf1 include:key-9283947588214 ?all"
```
