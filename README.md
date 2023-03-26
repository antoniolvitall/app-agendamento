# App para cadastro de profissional e consultas

## Setup

Primeira coisa a se fazer é clonar o repositório

```sh
$ git clone https://github.com/antoniolvitall/app-agendamento.git
```
Faça o download do python em https://www.python.org/ e instale em sua máquina.

Crie um ambiente virtual com o python.

```sh
$ python -m venv venv
```

Ative o ambiente virtual do python com os seguintes comandos:
-Para Windows
```sh
$ .venv/Scripts/Activate
```
-Para MAC e Linux:
```sh
$ .venv/bin/activate
```

Dentro do ambiente virtual, instale o Django e o Django Rest Framework.
```sh
(env)$ pip install pip install django
(env)$ pip install pip install djangorestframework
```
Note que `(env)` na frente do terminal indica que vocês está com o ambiente virtual ativo.

Depois que o `pip` terminar de instalar o Django e o Django Rest Framework, utilize os comandos para iniciar o servidor.

```sh
(env)$ cd myproject
(env)$ python manage.py runserver
```
E, para uma visualização mais simples, abra o link `http://127.0.0.1:8000/admin/`.
O login e senha são `admin` e `admin`.

Espero que gostem!
