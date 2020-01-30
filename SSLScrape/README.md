# SSLScrape

## O que é
O **SSLScrape** é uma ferramenta de varredura que nos auxilia a rastrear nomes de host através de certificados SSL. Ele foi desenvolvido por **Peter Kim** que é autor do livro **The Hacker Playbook** e o **@bbuerhaus** que é o CEO da **Secure Planet LLC**.

## Sobre o projeto
O projeto pode ser encontrado no github no seguinte link
```sh
https://github.com/cheetz/sslScrape
```

Ele foi desenvolvido em Python.

## Usando Docker
Como o projeto é em Python e precisa instalar algumas bibliotecas podemos usar o docker para não precisar instalar os requisitos em nossa máquina.

O Dockerfile é o seguinte
```sh
FROM python:alpine
WORKDIR /root
COPY . .
RUN pip3 install censys
ENTRYPOINT ["python3","script-censys.py"]
```

Podemos realizar o build da imagem da seguinte forma
```sh
sudo docker build -t "greenmind/sslscrape:1" .
```

Podemos agora usar a imagem e ainda passar via argumento a ferramenta.
```sh
sudo docker container run -it --rm "greenmind/sslscrape:1" 37.59.0.0/16
```
