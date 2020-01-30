## O que é o Censys
Censys que foi criado em 2015 na universidade de Michigan, ele nos auxilia na busca de dispositivos , redes e infraestruturas.

![Censys 1](https://i.imgur.com/4OHE97L.png)

**45 das Fortune 500 usa dados do Censys**.
> Fortune 500 é uma revista que lista as 500 maiores corporações em todo o mundo.

![Censys 2](https://i.imgur.com/adbIJGo.png)

## Como podemos usar o Censys
Agora com a ajuda desse mecanismo de busca podemos encontrar facilmente informações como
- Latitude
- Longitude
- País
- Rota
- Portas abertas e protocolos
- Podemos ver o tipo de servidor usado
- Status do teste
- Titulo do IP usado
- Nome da rede  de sites e IPS.
- Identifica

![Censys 3](https://i.imgur.com/tmahhSn.png)

E podemos obter essas informações sem estar logado no censys, podemos criar uma conta free e já começar a usar.

## Já logado no sistema
Logado no sistema podemos já realizar consultas de **whois** , podemos obter informações nos formatos:
- Table
- JSON
- Raw WHOIS

Exemplo usando o site da globo.com:
```sh
https://censys.io/ipv4/186.192.90.5/whois
```

Além disso podemos encontrar:
- Informações básicas do domínio
- Informações de contato
- Informações sobre a rede
- Informações técnicas
- Informações administrativas
- Contato para relatar algum abuso

O que podemos fazer com essas informações ?
- Obter emails
- Obter range de rede e descobrir outros servidores
- CIDR , podemos encontrar outros servidores na mesma rede

## Buscando informações sobre sites
Podemos usar a opção de site que fica disponível em:
```sh
https://censys.io/domain?q=globo.com
```

Ao pesquisar temos vários resultados de sites , o primeiro foi o que nós buscamos e além disso temos as seguintes informações:
- Protocolos
- Tags
- Resultados
- Report
- Documentação

![Censys 4](https://i.imgur.com/YIk4W6s.png)

Ao selecionar o nosso site temos informações como
- Alexa rank
- Protocolos disponível
- Informações sobre as portas que estão abertas
- Qual o servidor usado
- Titulo do site
- Informações sobre certificados do HTTPS
- Banner do serviço
- Configurações de DNS

Veja usando como exemplo o site da globo.com
![Censys 5](https://i.imgur.com/yGrwWOl.png)

Além disso essas informações podem ser nos formatos
- JSON
- Tabelas

## Buscando informações sobre certificados
Podemos ver informações sobre certificados usando o seguinte link
```sh
https://censys.io/certificates?q=globo.com
```

![Censys 6](https://i.imgur.com/LmMFHLl.png)

## Censys API
Podemos usar o poder do Censys usando a API dele , dessa forma podemos criar ferramentas e até inserir em outros projetos.

Podemos ver a documentação em
```sh
https://censys.io/api
```

> Precisamos criar uma conta no Censys, com ela temos acesso a informações da conta , **API ID** , **Secret** , limites da conta.

## Criando conta
Podemos criar uma conta Free no seguinte link
```sh
https://censys.io/register
```

> Pode ser necessário validar a conta no seu email , caso não queira usar o seu email é possível usar **https://10minutemail.net/?lang=pt-br**.

### Informações de conta
Depois de criar uma conta podemos ir no link abaixo e ver informações da conta.
```sh
https://censys.io/account
```

Podemos encontrar informações como
- Nome
- Email
- Login
- Afiliação
- Telefone
- Mudar a senha
- Porcentagem de uso do plano
- Quando vai ser reiniciado o plano
- Tipo de plano
- Informações sobre resultados

### Informações sobre API
```sh
https://censys.io/account/api
```

No link acima é possível obter as credenciais para o uso da API e além disso podemos encontrar
- API ID
- Secret
- Observar limites da conta
- Resetar as chaves da API

### Formas de pagamento
Temos uma conta free, porém podemos pagar uma conta Pro ou até Enterprise.
```sh
https://censys.io/account/billing
```

## Censys API + Python
É possível usar a API do censys com o Python.

Anteriormente já tivemos acesso as credenciais necessárias , agora vou mostrar a documentação do github.
```sh
https://github.com/censys/censys-python
```

E tem até alguns exemplos de uso.
> https://censys.io/api

### Criando codigo Python
Podemos criar um código em Python para automatizar a consulta e além disso também vamos usar argumentos para que possamos usar o código de forma fácil.
```python
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
```

### Criando imagem Docker
Com o código que criamos anteriormente conseguimos criar uma imagem no docker e assim automatizar a criação da infraestrutura.
```sh
FROM python:alpine
WORKDIR /root
COPY . .
RUN pip3 install censys
ENTRYPOINT ["python3","script-censys.py"]
```

Vamos realizar o build da imagem
```sh
sudo docker build -t "greenmind/censys:1" .
```

Podemos usar a imagem criada anteriormente da seguinte forma
```sh
sudo docker run -it --rm "greenmind/censys:1" 37.59.174.225
```

### Projeto gelim/censys
Podemos usar um projeto bem interessante que está disponível no Github , ele nos auxilia para o uso da API do Censys com a linguagem python e ainda disponibiliza uma documentação.
```sh
https://github.com/gelim/censys
```
