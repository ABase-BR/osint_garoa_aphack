
## Antes de começar
**Whois** ou **quem é?** é um protocolo TCP que funciona por padrão na porta **43** e usamos para consultar informações de um determinado IP ou domínio.

## O que podemos encontrar com o Whois ?
Podemos encontrar informações como
- Nome do domínio
- Quem registrou o domínio
- Quando foi criado
- Até quando é valido
- Servidores DNS
- Pais
- email de contato
- Nome do responsável
- CPF/CNPJ

Alguns sites podem ter configurado para não mostrar informações do proprietário e onde podemos buscar essas informações de forma publica ?

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
- Pais

Podemos testar usando o hackertarget
```sh
https://hackertarget.com/whois-lookup/
```

## Usando o python

### Buscando informações sobre dominios
Podemos automatizar tarefas usando o Python, dessa forma usando a API do **hackertarget** podemos buscar informações sobre dominios e IPS.

Por exemplo, vamos buscar informações do dominio **businesscorp.com.br**.
```python
import requests

r = requests.get('https://api.hackertarget.com/whois/?q=businesscorp.com.br')

#print(r.status_code)
print(r.text)
#print(r.headers['content-type'])
```

### Buscando informações sobre IPS
Agora vamos buscar informações sobre um dominio especifico.
```python
import requests

r = requests.get('https://api.hackertarget.com/whois/?q=37.59.174.225')

#print(r.status_code)
print(r.text)
#print(r.headers['content-type'])
```

## Usando o Docker

### Projeto IP
#### Criando imagem
Podemos criar a imagem usando:
```sh
sudo docker build -t "greenmind/whois:ip" .
```

#### Realizando teste
Podemos usar o docker para realizar o teste:
```sh
sudo docker run -it --rm "greenmind/whois:ip" 37.59.174.225
```

### Projeto URL
#### Criando imagem
Podemos criar a imagem usando:
```sh
sudo docker build -t "greenmind/whois:url" .
```

#### Realizando teste
Podemos usar o docker para realizar o teste:
```sh
sudo docker run -it --rm "greenmind/whois:url" businesscorp.com.br
```
