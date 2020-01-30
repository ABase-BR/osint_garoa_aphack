# Yandex (Russia)
```sh
https://yandex.com/
```

Yandex é uma companhia russa que opera o maior motor de busca da Russia e detêm 60% do mercado no país.

Podemos usar operadores nele e nos ajuda a trazer informações interessantes.

## Operador (Site)
Podemos passar o operador **site** e passar um determinado site.

Por exemplo
```sh
site:businesscorp.com.br
```

## Python + API
Vamos usar uma biblioteca chamada **yandex-search**.
> https://pypi.org/project/yandex-search/

Podemos instalar ela usando o **pip3**.

Podemos criar uma conta no yandex no seguinte link:
```sh
https://passport.yandex.ru/registration
```
> O site é em russo

Podemos ver as configurações em
```sh
https://xml.yandex.ru/settings.xml
```
> Vá até **Settings**.

Vamos começar o código, já vou iniciar ele com argumento e assim podemos passar os alvos via argumento.
```python
import yandex_search
import sys

if len(sys.argv) >= 2:
    #print(sys.argv[0])
    site = sys.argv[1]
    yandex = yandex_search.Yandex(api_user='my-user', api_key='mykey')
    print(yandex.search('site:'+site).items)
else:
    print("algo deu errado")
```

## Python + API + Docker
Já com o código criado, vamos agora criar nossa imagem docker.
```sh
FROM python:3-slim-stretch
RUN pip3 install yandex-search
WORKDIR /root
ADD . .
ENTRYPOINT ["python3","yandex-site.py"]
```

Podemos realizar o build dessa imagem.
```sh
sudo docker build -t "greenmind/yandex:1" .
```

Podemos usar a imagem da seguinte forma.
```sh
sudo docker container run -it --rm "greenmind/yandex:1" businesscorp.com.br
```
