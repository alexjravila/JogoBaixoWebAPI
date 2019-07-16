# Jogo baixo Web API
Este projeto é uma Web API desenvolvida em Python para o projeto **Jogo baixo**. 

## Tecnologias
- Python 3;
- Flask;
- Connexion;
- Swagger;
- Pytest;
- Coverage.

## Getting start
1. Acessar ambiente virtual (ver arquivo na task de como fazer isso);
2. Executar o comando para instalar as dependências do projeto:
    ``` sh
    pip install -r requirements.txt
    ```
3. Para executar o projeto, execute o comando
    ``` sh
    python run.py
  
    ```
4. URL: http://localhost:5000/
5. Swagger UI: http://localhost:5000/api/ui/

## Outros comandos
- Executar testes automatizados:
    ``` sh
    pytest
    ```
- Coverage dos testes:
    ```
    coverage run -m pytest
    ```
- Relatório do coverage de testes:
    ```
    coverage report
    ```

## Docker
 Existe a possível rodar a aplicação e container do Docker. Utilizando um exemplo simples de container baseado em uma imagem do Python 3 Alpine. Todas as configuração do container então no Dockfile da aplicação.
 
 1.  O primeiro passo é desabilitar o modo DEBUG no arquivo **run.py**.

 2. É necessario fazer o build da imagem, para isso é só executar o comando abaixo:
     ``` sh
    docker build -f Dockerfile -t jbapi/python:3-alpine .
    ```
 3. Depois da imagem construida, é possível criar um container tendo ela com base e executar a aplicação:
     ``` sh
    docker run -p 8080:5000 jbapi/python:3-alpine
    ```

## Observações
1. Toda pasta dentro da pasta app deve ter um arquivo **__init\__.py**. Isso indica que a pasta é um módulo e pode ser devidamente importado e utilizado por outros arquivos de código.
2. Para injetar parâmetros nos testes automatizados, deve ser definido uma fixture no arquivo **conftest.py**. O nome do parâmetro deve ser o mesmo da fixture (ver o caso do parâmetro client nos testes da view).
3. Todo endpoint deve ser definido no arquivo **swagger.yml**.

## Links para estudos
- [Tutorial Flask](https://code.tutsplus.com/pt/tutorials/building-restful-apis-with-flask-diy--cms-26625)
- [Repositório projeto connexion](https://github.com/zalando/connexion)
- [Tutorial connexion](https://realpython.com/flask-connexion-rest-api/#adding-connexion-to-the-server)
- [Exemplo projeto connexion](https://github.com/realpython/materials/tree/master/flask-connexion-rest/version_4)
- [Tutorial pytest](https://blog.cedrotech.com/pytest-faca-testes-e-gere-relatorios-rapidamente/)
- [Documentação do test client do flask](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_client)
- [Tutorial de uma api flask com testes automatizados](http://flask.pocoo.org/docs/1.0/testing/#testing)
- [Projeto de exemplo da api flask com testes automatizados](https://github.com/pallets/flask/tree/1.0.2/examples/tutorial)