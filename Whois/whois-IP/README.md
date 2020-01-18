# Usando o Docker

## Criando imagem
Podemos criar a imagem usando:
```sh
sudo docker build -t "greenmind/whois:ip" .
```

## Realizando teste
Podemos usar o docker para realizar o teste:
```sh
sudo docker run -it --rm "greenmind/whois:ip" 37.59.174.225
```
