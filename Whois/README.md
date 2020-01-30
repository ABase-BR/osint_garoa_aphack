## Antes de começar
**Whois** ou **quem é?** é um protocolo TCP que funciona por padrão na porta **43** e usamos para consultar informações de um determinado IP ou domínio.

## O que podemos encontrar com o Whois ?
Podemos encontrar informações como
- Nome do domínio
- Quem registrou o domínio
- Quando foi criado
- Até quando é válido
- Servidores DNS
- País
- email de contato
- Nome do responsável
- CPF/CNPJ

Alguns sites podem ter configurado para não mostrar informações do proprietário e onde podemos buscar essas informações de forma pública ?

Temos diversos sites , segue dois exemplos
```sh
https://hackertarget.com/whois-lookup/
https://br.godaddy.com/whois
```

Além dos domínios também podemos pesquisar por IPS , dessa forma podemos buscar informações sobre a rede e assim encontrar informações como
- Range de rede
- CIDR
- Organização responsável
- Endereço
- Cidade
- País

Podemos testar usando o hackertarget
```sh
https://hackertarget.com/whois-lookup/
```

## Usando o python
Podemos automatizar a coleta de informações usando a linguagem python, vamos usar ela pois alem de ser uma linguagem com uma incrivel curva de aprendizado é muito poderosa.

### Buscando informações sobre dominios
Podemos automatizar tarefas usando o Python, dessa forma usando a API do **hackertarget** podemos buscar informações sobre dominios e IPS.

Por exemplo, vamos buscar informações do domínio **businesscorp.com.br**.
```python
import requests

r = requests.get('https://api.hackertarget.com/whois/?q=businesscorp.com.br')

#print(r.status_code)
print(r.text)
#print(r.headers['content-type'])
```

Podemos melhorar o código acima usando argumentos, o código fica da seguinte forma:
```python
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
```

### Buscando informações sobre IPS
Agora vamos buscar informações sobre um domínio específico.
```python
import requests

r = requests.get('https://api.hackertarget.com/whois/?q=37.59.174.225')

#print(r.status_code)
print(r.text)
#print(r.headers['content-type'])
```

Assim como a busca de informações sobre domínios, podemos também buscar informações sobre IPS e também passar o alvo como argumento.
```python
import requests

import sys

if len(sys.argv) >= 2:
    #print(sys.argv[0])
    ip = sys.argv[1]
    r = requests.get('https://api.hackertarget.com/whois/?q='+ip)

    #print(r.status_code)
    print(r.text)greenmind/whois:ip
    #print(r.headers['content-type'])
else:
    print("algo deu errado")
```

## Projeto IP
### Criando imagem
Podemos criar a imagem usando:
```sh
sudo docker build -t "greenmind/whois:ip" .
```

### Realizando teste
Podemos usar o docker para realizar o teste:
```sh
sudo docker run -it --rm "greenmind/whois:ip" 37.59.174.225
```

## Projeto URL
### Criando imagem
Podemos criar a imagem usando:
```sh
sudo docker build -t "greenmind/whois:url" .
```

### Realizando teste
Podemos usar o docker para realizar o teste:
```sh
sudo docker run -it --rm "greenmind/whois:url" businesscorp.com.br
```
