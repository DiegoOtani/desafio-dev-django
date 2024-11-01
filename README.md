# Desafio Técnico Desenvolvedor Django - DIGITAL SYS

Este é um projeto de API RESTfull desenvolvido com Django e Django REST Framework. A API fornece endpoints para criar, ler, atualizar e excluir (CRUD) recursos e pode ser usada como base para desenvolvimento de APIs em Django. Trata de um sistema de cadastro de currículos, permitindo o cadastro de informações pessoais, contato, experiência profissional e formação acadêmica.

## Funcionalidades

- Cadastro, atualização, listagem e remoção de registros.
- Validação e tratamento de erros.
- CRUD completo de dados pessoais, contato, experiência profissional e formação acadêmica.

## Tecnologias usadas

- Django: Framework principal para desenvolvimento da aplicação.
- Django REST Framework: Fornece as ferramentas para construção de APIs RESTful.
- SQLite: Banco de dados (configurável para outros bancos como PostgreSQL).

## Instalação e Configuração

### Pré-requisitos
- Python
- pip

### Passo a passo
#### 1. Clone o repositório:

```
git clone https://github.com/DiegoOtani/desafio-dev-django.git
cd desafio-dev-django
```

#### 2. Execute as migrações:

```
python manage.py migrate
```

#### 3. Crie um administrador(opcional para acessar o painel de administrador):

```
python manage.py createsuperuser
```

*Observação:
##### O projeto possui um ADMIN padrão configurado:
```
username: digital-sys
password: sys123456
```
#### 4. Inicie o servidor:

```
python manage.py runserver
```