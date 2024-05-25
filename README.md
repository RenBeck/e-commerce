# E-commerce de Moda Online

Bem-vindo ao projeto de E-commerce de Moda Online, uma plataforma onde os clientes podem comprar produtos de moda, incluindo roupas, acessórios e calçados. Este README fornecerá uma visão geral do projeto, como configurá-lo e usá-lo.

## Índice

1. [Visão Geral do Projeto](#visão-geral-do-projeto)
2. [Requisitos](#requisitos)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Execução](#execução)
6. [Testes](#testes)
7. [Funcionalidades](#funcionalidades)
8. [API](#api)
9. [Contato](#contato)

## Visão Geral do Projeto

Este projeto é uma plataforma de e-commerce desenvolvida com Django, que permite aos clientes comprar produtos de moda online. A plataforma destaca a variedade de produtos disponíveis, incluindo roupas, acessórios e calçados. Os clientes podem se registrar, pesquisar produtos, adicionar itens a sacola de compras, efetuar pagamentos e gerenciar suas informações pessoais. Colaboradores podem gerenciar produtos e vendas.

## Requisitos

- Python 3.12.0
- Django 5.0.1
- PostgreSQL 
- Pip 

## Instalação

### Clone o Repositório

```bash
git clone git@github.com:RenBeck/bs-ecommerce.git
cd bs-ecommerce
```

### Crie e Ative um Ambiente Virtual

Usando venv e pip:

```bash
python -m venv venv
source venv/bin/activate # No Windows use`venv\Scripts\activate`
pip install -r requirements.txt
```

### Migrações do Banco de Dados

Aplique as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

### Crie um Superusuário

Crie um superusuário para acessar o Django Admin:

```bash
python manage.py createsuperuser
```

## Execução

### Execute o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Acesse o site em http://localhost:8000.

## Testes

### Rodando Testes Automatizados

Para rodar os testes automatizados, use:

```bash
python manage.py test
```

### Testes Implementados

- Testes de Views: Garantem que as views estão retornando os dados corretos.
- Testes de Models: Verificam a integridade dos modelos e suas interações.
- Testes de Forms: Validam a funcionalidade dos formulários.
- GitHub Actions: CI/CD configurado para rodar testes automaticamente a cada push.


## Funcionalidades

- Página Inicial: Apresenta informações sobre a empresa e destaques de produtos.
- Sistema de Cadastro e Login: Permite que usuários se registrem e façam login.
- Pesquisa de Produtos: Funcionalidade para buscar produtos.
- Sacola de Compras: Adicionar e remover produtos na sacola de compras.
- Processamento de Pagamentos: Integração com gateway de pagamento.
- Área do Usuário: Ver sacola, histórico de compras e dados pessoais.
- Variedade de Produtos: Destaque para a variedade de produtos disponíveis, incluindo roupas, acessórios e calçados.

## API

A aplicação utilizada   para gerenciamento de vendas da PagSeguro.

Este README oferece uma visão completa do seu projeto de E-commerce de Moda Online, desde a instalação e configuração até os testes e a estrutura do código, facilitando a vida dos colaboradores e usuários.

## Contato

Para mais informações ou questões, entre em contato:

WhatsApp: (31)984987998
