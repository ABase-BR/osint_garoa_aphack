# robots.txt

## O que é
O robots.txt é um arquivo que costuma ser encontrado na raiz do servidor web e é resposavel por dizer o que deve ou não ser indexado nos motores de busca. Dessa forma ele é resposavel pelo o que vai ser indexado ou não será. Os bots crawlers de motores de busca como Google analisa esses arquivos e se não for configurado corretamente pode acabar indexando diretorios importantes.

## Comandos basicos

### User-agent
Com o comando **User-agent** é resposavel por determinar qual bot de busca você está se referindo. Podemos conhecer todos os nomes de **User-agent** no endereço:
[Web Robots Database](https://www.robotstxt.org/db.html)


### Disallow
Com o comando **Disallow** conseguimos descrever quais **páginas**, **diretórios** ou até **sites** não queremos adicionar nos resultados de busca.

### Allow
Já com o comando **Allow** conseguimos informar para os bots de busca quais são as páginas e os diretórios do site você deseja que sejam indexadas.

Com o uso do comando **Allow** é recomendado usando bloqueamos uma pasta ou diretório através do Disallow. Assim conseguimos indexar apenas um arquivo ou até uma pasta específico que está dentro da pasta/diretório bloqueado.

## Buscando por arquivos
Já na hora de realizar um reconhecimento de uma infraestrutura podemos usar esses comandos a nosso favor para buscar arquivos e diretorios que os administradores não queiram que sejam indexados. Dessa forma podemos buscar por diretorios contendo backups, imagens, documentos e até contratos que não deveriam estar disponiveis no nos motores de busca. Mas graças ao robots.txt podemos buscar por arquivos.

### Exemplo de busca
Podemos buscar pelo arquivos indo até o site e passando no final o robots.txt.
```sh
http://businesscorp.com.br/robots.txt
```

Nesse exemplo conseguimos encontrar 5 configurações e são elas.
```sh
User-agent: *
Disallow: /_restrito
Disallow: /_docs
Disallow: /admin
Disallow: /bkp
Allow: /configuracoes/comunicacao/projeto.txt
```
> No exemplo acima conseguimos encontrar diretorios restritos, documentos, diretorio de admin, backups que não queriam que fosse encontrado. Alem disso temos o Allow falando que indexar esse arquivo txt no google.

### Referencia
- https://suporte.hostgator.com.br/hc/pt-br/articles/115000452673-Como-funciona-o-arquivo-robots-txt
- https://www.robotstxt.org/db.html
