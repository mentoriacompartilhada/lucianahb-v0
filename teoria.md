# API

Rest trabalha em cima do protocolo http 
    verbos: 
- get (leitura, não passo body)
- post (crio novo conteúdo)
- post
- put (submete tudo mesmo alterando só um campo)
- patch (em vez de eu submeter o conteúdo todo, aplico só a alteração sobre o conteúdo original)
- delete (não recebe corpo, preciso informar o servidor qual dado será removido)
- options (é automático, usado na parte de segurança, opções do que é aceito)

> API precisa ser autodescritiva (preciso ler a url e saber o que está acontecendo)

## Protocolos
>https://http.cat/
- 1 - informação
- 2 - sucesso
- 3 - redirecionamento
- 4 - erro do client
- 5 - erro do servidor


> Pequisar - github action - automatiza ações da api


> gitignore.io - https://www.toptal.com/developers/gitignore


- virtualenv --python=python3.9 venv
- source venv/bin/activate 
- pip install django djangorestframework
- (para rodar os requirements) pip freeze > requirements.txt


# Aula 2
## To do
- nome 
- sobrenome
- email
- senha

#Aula 3

httpbin.org - ajuda com requisições http. No postman passo o httpbun.org/get ou qualquer outro verbo

- Fazer Paginação (commit Gui)

#Aula 4
- Baixar Postman
- https://randomuser.me/
- WSL: Windows subsystem for linux
- windows terminal (posso trocar entre terminais - bash, powershell)


#Aula 5 (22/09/2021)
 - Continuação em paginação
 - Acompanhar commits de hoje no projeto do Gui
> Pequisar - Hateoas (REST API)


#Aula 6 (17/11/2021)

##Manipulação de Arquivos
 - antes de ler um arquivo, checar se ele existe
 - se for escrever um arquivo, ver se tenho permissão
 - escrever em pasta, ver se ela existe
 - import os, 'r', 'w', 'a', 'x'
 
 - \r carriage return (Unix) e \n carriage return line feed
    - Como o nome diz o CR faz voltar para o início da linha e o LF é para ir para a próxima linha.