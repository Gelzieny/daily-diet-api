# daily-diet-api

## 📋 Regras da aplicação

- Deve ser possível registrar uma refeição feita, com as seguintes informações:
  - Nome
  - Descrição
  - Data e Hora
  - Está dentro ou não da dieta
- Deve ser possível editar uma refeição, podendo alterar todos os dados acima
- Deve ser possível apagar uma refeição
- Deve ser possível listar todas as refeições de um usuário
- Deve ser possível visualizar uma única refeição
- As informações devem ser salvas em um banco de dados

## 📚 Documentação da API:


## 🛠️ Tecnologias Utilizadas:
A Daily Diet API utiliza as seguintes tecnologias:

- **Flask**: Micro-framework web para Python.
- **Flask-Login**: Gerenciamento de sessões de login.
- **SQLAlchemy**: ORM (Object Relational Mapper) para interação com o banco de dados.
- **Werkzeug**: Biblioteca para manipulação de senhas (hashing).
- **Docker**: Contêinerização para facilitar a execução do projeto em qualquer ambiente.

### Pré-requisitos

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,vscode,python,postman,docker" />
</a>

### Clone o repositório

````bash
# Clone este repositório
$ git clone <https://github.com/Gelzieny/daily-diet-api.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd daily-diet-api
````
### Configuração do Ambiente

````bash
# Acessando o Shell
$ flask --app src.app.py shell

# Crie e ative um ambiente virtual e Instale as dependências
# No Windows
$ python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# No Linux/Mac 
$ python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Rodar o docker-compose
$ docker-compose up -d
````
### Executando o  flask shell

````bash
# Enters the flask shell on the terminal
$ flask shell

# Creates database
$ db.create_all() #create tables
$ db.session.commit() # commits changes

# create user
$ user = User(username="admin")
$ db.session.add(user)
$ db.session.commit()

$ exit() #quits flask shell
````

### Executar projeto

````bash
# Para roda o projeto
$ python src/app.py
````