# Whatcms

## Mas o que é whatcms?
Projeto lançado em dezembro de 2011 que nos auxilia no reconhecimento de CMS, com ele conseguimos realizar a verificação de qual sistema ele está usando e sem ao menos interagir diretamente com ele.

Com ele conseguimos reconhecer mais de 422 CMS e alguns deles são:

- wordpress
- joomla
- moodle
- Drupal
- PhpBB

Podemos usar ele sem cadastro usando o site
```sh
https://whatcms.org/
```

Caso queira usar a API podemos realizar o cadastro:
```sh
https://whatcms.org/API?cmd=RegisterForm
```
> O cadastro é gratuito

Também podemos usar as versões pagas por **10 dólares** por mes conseguindo verificar **10 mil sites** e até **360 dólares** por mês conseguindo verificar mais de **1 milhão de sites**.
```sh
https://whatcms.org/Subscriptions/Plans
```

## Como ele reconhece ?
Graças a **analise de metadados**, **headers da aplicação** e **arquivos javascript** ele consegue identificar um CMS.

- https://whatcms.org/Tech_Reports

## Whatcms - Reconhecimento CMS + API
Podemos usar o python3 para automatizar a coleta de informações do whatcms e graças a API conseguimos agilizar nosso trabalho.

O que precisamos saber ?
- Realiza 1000 (mil) requisições por mês
- 1 requisição a cada 10 segundos

> Mais informações em:
- https://whatcms.org/API

## Automatizando teste usando python3
Podemos usar o python para criar um programa e assim nos auxiliar na consulta do whatcms.

Vou usar o **python3** e uma biblioteca chamada **pywhatcms**.
```python3
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
```

Para o programa funcionar corretamente precisamos instalar uma biblioteca, vamos usar o **pip3** para realizar a instalação.
```sh
pip3 install pywhatcms
```

Podemos agora executar o programa.
```sh
python3 script-whatcms.py s3cr3t-k3y-4p1 https://alvo
```

## Lab usando Docker
Além de automatizar a consulta, podemos também automatizar a nossa infraestrutura.

Para isso vamos usar o docker e agora vamos criar um arquivo **Dockerfile** para criação da infraestrutura.
```sh
FROM python:alpine
WORKDIR /root
COPY . .
RUN pip3 install pywhatcms
ENTRYPOINT ["python3","script-whatcms.py"]
```

Para a criação da imagem vamos usar o build.
```sh
sudo docker build "greenmind/whatcms:1" .
```

Como usamos o **ENTRYPOINT** no arquivo **Dockerfile** conseguimos usar nosso programa com argumentos no docker.
```sh
sudo docker container run -it --rm "greenmind/whatcms:1" s3cr3t-k3y-4p1 https://alvo
```

## Documentação oficial
Conseguimos ver mais informações na documentação oficial, lá temos todas as informações necessários para começar a usar o whatcms e podemos realizar a consulta usando:
- curl
- PHP Wrapper

> Veja mais informações em:
- https://whatcms.org/Documentation

## Outros projetos
- https://github.com/HA71/pywhatcms
