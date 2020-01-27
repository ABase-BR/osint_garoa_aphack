# O que é crt.sh
O **crt.sh** é uma ferramenta para nos auxiliar na busca de subdominios usando a coleta da informações de certificados.

## Como funciona ?
O crt.sh usa logs publicos para buscar por informações, devido ao Transparência do certificado (CT) que visa criar um sistema de logs públicos, assim buscando registrar todos os certificados emitidos por autoridades de certificação confiáveis e assim permitindo a identificação eficiente de certificados emitidos por engano ou maliciosamente.

## Site oficial
Podemos encontrar o projeto no seguinte site:
```sh
https://crt.sh/
```

## Automatizando a coleta
Podemos usar o site para a coleta de informações, mas e se quiser automatizar ?

Podemos usar algumas formas, são elas:
- ShellScript
- Docker

Em todos os processos vamos precisar dos requisitos:
- curl (Para realizar as consultas)
- jq (Para realizar o parse de json)


### Shell Script
Podemos usar ShellScript para automatizar a busca, vamos iniciar com uma linha.

#### One-line
Podemos realizar consultas usando apenas uma linha.
```sh
curl -s 'https://crt.sh/?q=%.google.com&output=json' | jq '.[] | {name_value}' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | sed 's/name_value: //g'
```

#### Projeto .sh usando argumentos
Outra forma é criando um codigo e passando o alvo como argumento:
```sh
#!/bin/bash

# check arg
if [[ "$1" == "" ]]
then
  echo "Não foi passado nenhum argumento"
else
  ALVO="$1"
  URL='https://crt.sh/?q=%.'$ALVO'&output=json'
  curl -s $URL | jq '.[] | {name_value}' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | sed 's/name_value: //g'
fi
```

> No meu caso chalei esse projeto de **crt.sh**, precisamos dar permissão de execução e pode ser feito usando:
```sh
chmod +x crt.sh
```

Podemos executar ele da seguinte forma:
```sh
./crt.sh google.com
```

### Usando o docker
Podemos usar o docker, dessa forma usamos ele de forma isolado e não precisamos instalar nada em nossa maquina.

> Já desenvolvi um projeto que pode ser encontrado em
```sh
https://github.com/greenmind-sec/crt.sh-docker
```

#### Dockerfile
Inicialmente criamos um arquivo Dockerfile que criamos a infraestrutura necessario.
```sh
FROM alpine:3.10

RUN apk add --no-cache curl jq

WORKDIR /root

ADD . .

RUN chmod +x crt.sh

ENTRYPOINT ["sh","/root/crt.sh"]
```
> Com o uso do **FROM** setamos uma imagem, nesse caso vou usar um alpine, **RUN** executa comando e nesse caso vou instalar os requisitos para ele funcionar que é **curl jq**. Já o comando **WORKDIR** vamos usar para falar que queremos ir para um determinado diretorio, nesse caso é o **/root**. O **ADD** vai adicionar um arquivo ou varios. Usamos novamente o **RUN** para dar permissão de execução no programa **crt.sh** e para finalizar usamos o **ENTRYPOINT** que vai setar o nosso script. Dessa forma podemos usar argumentos nesse container e ele só tem 8 MB.

#### Compilando imagem
```sh
sudo docker build -t "greenmind/crt.sh:1" .
```

#### Usando a imagem
Podemos usar ela passando o alvo argumento.
```sh
docker run -it --rm "greenmind/crt.sh:1" "google.com"
```

## Referencias
> https://en.wikipedia.org/wiki/Certificate_Transparency
