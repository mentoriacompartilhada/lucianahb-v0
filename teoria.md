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


# Aula 2
## To do
- nome 
- sobrenome
- email
- senha
