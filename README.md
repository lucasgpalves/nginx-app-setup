## Nginx+FastAPI+Redis

Esse repositório é um relato de expêrincia, demonstrando como fiz o deploy utilizando docker compose, dentro de uma VM.

## Tecnologias/Ferramentas
- VSCode
- Docker
- Nginx
- FastAPI
- Redis
- VirtualBox Machine

## Processo
Fiz esse projeto para iniciar o uso de Nginx, configurações iniciais, além de aprender a estruturar uma API, uma estrutura mais limpa de projeto. Quis também testar meus conhecimentos de Docker, evitei pesquisar na internet, procurando identificar, se eu já conseguia utilizar o essencial do docker, subir conteineres, navegar neles, executar eles internamente e capturar informações importantes a partir do `docker ps` e `docker logs`.

Além manter meu projeto, pois essa arquitetura de API, eu havia criado esse repositório a uns 3 meses, nunca mais tinha tocado nesse código, logo tive que adaptar ele para este projeto. `root_path` é um parâmetro muito importante, para que eu consiga ter uma estrutura separada para a minha API, utilizando o versionamento `/api/v1/`.

### Desenvolvimento da API
Contexto, eu comecei desenvolvendo API utilizando Java e Spring Boot, realmente acho a forma de estruturar projetos utilizando essa separação muito eficiente, era a maneira como me organizo. Como essa é uma API bem do meu começo, onde ainda estava entendendo o funcionamento de alguns recursos do FastAPI e integração com bancos de cache.

Utilizei uma estrutura parecida com MVC, porém adaptada, utilizei um core e repositories, para abstrair mais o código, torna ele mais complexo, porém quando dá o problema, é possível encontrar ele mais facilmente no código. Contudo, fiz a abstração apenas do que era necessário, nos arquivos `router.py` e `redis.py`, não vi como necessário criar uma estrutura de classe.

O projeto utiliza o Model `[example.py](./app/models/example.py)` como base. Há 3 requisições principais no arquivo `router.py`, uma que funciona como ping, outra para realizar a criação de um objeto e outra para retornar. O meu `service.py` é responsável por executar as ações solicitadas pela requisição, por manipular meus objetos.

Isso me gerou um projeto, simples, porém bem estruturado, em decorrência da necessidade. 

### Repositório Nginx
A parte mais importante era o arquivo de configuração `nginx.conf`. Como minha inteção era ter uma página web e uma API rodando, foi definido duas locations: `/` e `/api/v1`, a `/` redireciona para um arquivo `index.html` para exibir que está em funcionamento (Não sou muito bom em fazer coisas de Frontend *risadas) e a `/api/v1` direciona para o meu conteiner com a API rodando.

Como o Nginx se encarrega de configurações mais complexas, não precisei fazer mais alterações além do `proxy_set_header`, para fazer o meu proxy reverso. Caso eu tivesse utilizado Kubernetes ou criado mais conteineres, poderia estar balanceando a carga entre eles.

### Gerando compose.yml
Diria que essa foi a parte mais tranquila, apenas declarar o que eu ia utilizar e a ordem que deveria ser criada. Criar primeiro meu "banco", logo em seguinda instanciar minha aplicação e depois subir meu conteiner web. Com isso em mente usei o `depends_on` para determinar a ordem que eu gostaria que fossem gerado os conteineres.

Gerei apenas o `app.dockerfile`, pois eu gostaria de iniciar meu conteiner app, com minha aplicação rodando e com algumas configurações de versão. Além do meu `.dockerignore`, para que não fossem coisas desnecessárias para minha VM, como meus arquivos de `.env`, pastas do `__pycache__` e meu `.venv` (ambiente virtual.)
## Requisições

### Exemplo POST
``` bash
curl -X POST \
  http://192.168.1.10/api/v1/examples \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Exemplo 1",
    "value": 2
}'
```

### Exemplo GET
``` bash
curl -X GET \
  http://192.168.1.10/api/v1/examples 
```

### Hello World GET
``` bash
curl -X GET \
  http://192.168.1.10/api/v1/
```

### Page GET
``` bash
curl -X GET \
  http://192.168.1.10/
```