# Buscando leaks com Python

## Sumario

## O que é um Leak
**Leak** é um termo inglês e significa **vazar** ou **vazamento** e é usada para difinir quando temos algum vazamento de dados/informações.

## Estamos comentendo algum crime ?
Toda informação que é publica, disponivel na interner e sem nenhum mecanismo de seguraça podemos usar. O problema se enquadra quando usamos essas informações para beneficio proprio.

## Quais informações são importantes
Vazamento de dados pode ser um problema para as empresas, funcionários e clientes.

Vamos imaginar o vazamento de **credencias** de funcionarios sendo expostas pela internet, agora quanto mais permissão de acesso essa pessoa ter, mais problemas poderemos ter.

Outro problema é vamos imaginar um **backup** que acaba sendo inserido em algum diretorio de algum site, os resposaveis não configuram para que motores de busca indexem esse diretorio e ao realizar uma busca conseguimos encontrar esses dados. Um dump por exemplo de um banco de dados seria um prato cheio para que pessoas maliciosas consigam credencias de pessoas chaves de uma empresa.

## Alguns vazamentos conhecidos

- Uber (156 mil Brasileiros tiveram nomes,telefones e emails vazados)

- Netshoes (2 milhões de clientes)

- Facebook (Cambridge Analytica)

- Banco inter (19 mil correntistas)

- C&A (mais de 2 milhões de clientes)

## Buscando informações em motores de busca

### Buscando informações no Google
O google é um motor de busca muito conhecido e é dos mais utilizados, ele nos ajuda na busca de paginas na internet e dessa forma conseguimos tambem buscar informações importantes.

Vamos realizar uma pesquisa usando o operador **site**, com ele filtramos buscando informações de um dominio especifico. Por exemplo:
```sh
site:pastebin.com
```

Com o auxilio de operadores, conseguimos filtrar ainda mais as nossas pesquisas e assim conseguindo negar palavras chaves. Essa palavra chave é **-** somado com a palavra que gostaria de negar. Por exemplo:
```sh
site:pastebin.com -webmail
```

### Buscando informações em Pastebins
Sabemos buscar por um dominio, negar e se quisermos buscar por uma palavra especifica? Conseguimos usar o operador **"palavra"** e assim aumentando o nosso filtro de busca.
```sh
site:pastebin.com "leak"
```
> Podemos buscar melhorar nossa busca e assim conseguir filtrar melhor, buscando por exemplo por nomes de pessoas, empresas e até emails.
```sh
site:pastebin.com "leak" "@email-da-empresa.com"
```

## Outras soluções

### dehashed
O dehashed nos ajuda com a busca de possiveis vazamentos , precisamos passar qual dominio queremos testar
```sh
https://dehashed.com/search?query=uber.com
```

### intelx.io
intelx.io tambem nos ajuda a buscar informações , ele nos retorna possiveis pastes com possiveis informações.
```sh
https://intelx.io/?s=uber.com
```

### psbdmp
Podemos buscar por informações de duas formas com o **psbdmp** , a primeira é usando a API.
```sh
https://psbdmp.ws/api/search/uber.com
```

Ou podemos usar o site
```sh
https://psbdmp.ws
```

### grayhatwarfare
Com o grayhatwarfare podemos buscar por possiveis arquivos.

```sh
https://buckets.grayhatwarfare.com/results/uber.com
```
> Esse exemplo ele nos retorna diversos buckets da amazon.

## Usando python para automatizar buscas
Já vimos como fazer algumas busca na mão usando motores de busca, como podemos usar APIS para a coleta de informações e agora vamos automatizar as buscas com o uso de Python.

Python é uma linguagem que tem uma curva de aprendizado bem legal, alem de ser incrivelmente poderosa e com 3 linhas já conseguimos criar scripts fantasticos.

Vamos usar o Python na versão 3, todos os testes vão ser feitos usando containers Docker e vou passar uma pequena base de como usar.

### Montando laboratorio
> Vamos montar um laboratorio usando Docker para criar a infraestrutura necessario para o desenvolvimento.

#### Instalando o Docker
Esses testes serão realizados em distribuições baseados no Debian.

Inicialmente vamos instalar o **curl**.
```sh
sudo apt-get install curl
```
> Ele é um requisito para o proximo passo.

Agora vamos baixar um script de instalação automatica usando o **curl** e já jogar ele para o **sh**.
```sh
curl -fsSL http://get.docker.com | sh
```

Vamos adicionar o usuario ao grupo Docker
```sh
sudo usermod -aG docker $USER
```
> Não esqueça de reiniciar a maquina

#### Criando laboratorio Python
Podemos buscar por imagens disponiveis no docker hub, lá conseguimos encontrar imagens oficiais do Python para usarmos e assim não precisamos ter nada instalado na nossa maquina alem do **docker**.

Podemos encontrar imagens oficiais do Python em
```sh
https://hub.docker.com/_/python
```

As imagens docker funciona da seguinte forma, por exemplo:
```sh
python:3
```
> Python seria o **nome da imagem**, já **:3** seria uma tag que nos ajuda a diferenciar versões.

Para realizar o download da imagem podemos usar o comando
```sh
docker pull python:3
```
> Com o uso do comando **pull** conseguimos obter a imagem.

Já uma imagem em funcionamento podemos entender como container, precisamos saber que os containers trabalham de forma isolada e por isso precisamos criar **volumes** que vão apontar diretorios da nossa maquina host para dentro do container.

Para criar um volume vou usar como exemplo o meu diretorio na maquina host que fica em **/home/greenmind/codigos** e vai ser apontado para dentro do container no diretorio **/root**.
```sh
docker container run -v "/home/greenmind/codigos:/root" -it --rm python:3 bash
```
> Dessa forma todos os scripts que estiverem disponiveis em **/home/greenmind/codigos** vai ser lincado para o **/root**.

Precisamos saber que todos os container são descartaveis e sempre que desligado todos os dados deles serão perdidos. Para resolver isso conseguimos subir ele em background, setar um nome e depois ter acesso usando o comando **docker exec**.
```sh
docker container run -v "/home/greenmind/codigos:/root" -d -it --name lab-python python:3 bash
```
> Agora podemos ter acesso usando **docker exec -it lab-python bash**.
```sh
docker exec -it lab-python bash
```

### Realizando crawler no pastebin

#### pwnbin
Vamos iniciar clonando o projeto.
```sh
git clone https://github.com/greenmind-sec/pwnbin/
```

Vamos até o projeto **pwnbin**:
```sh
cd pwnbin
```

Vamos criar uma imagem usando o Docker:
```sh
docker build -t "greenmind/pwnbin:1" .
```

Vamos agora criar um volume do diretorio **/root** que é onde estamos salvando o output e criar uma conexão com o nosso host.
```sh
docker run -v"${PWD}:/root" -it "greenmind/pwnbin:1" -k leak,pass -o /root/teste.txt
```

Agora podemos subir um arquivo com essas palavras no pastebin que o **pwnbin** vai buscar reconhcer.
