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

## Configuração para o acesso UTP ao

### Instale as libs:

```bash
pip install qrcode[pil]
pip install pyot
```

### Entre no Shell do Django 

```bash
python manage.py shell
```

#### Digite o seguinte código:

```bash
>>> from django.contrib.auth.models import User
>>> from django_otp.plugins.otp_totp.models import TOTPDevice
>>> import qrcode 
>>> user = User.objects.get(username='Nome_Usuário')           
>>> device = TOTPDevice.objects.create(user=user, name='OTP Device')                                          
>>> url = device.config_url                                                               
>>> qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)   
>>> qr.add_data(url)
>>> qr.make(fit=True)
>>> qr_img = qr.make_image(fill_color="black", back_color="white")
>>> qr_img.show()
```

No final das digitação do codigo será exibido um QR-CODE para adicionar o dispositivo OTP, você pode verificar o OTP usando um aplicativo de autenticação compatível, como o Google Authenticator. Obtenha o código OTP gerado pelo aplicativo e insira-o quando solicitado. 

## Configuração do Action

### Gere a chave SSH no seu servidor sem senha

```bash
ssh-keygen -t rsa -b 4096 -C "seu-email@exemplo.com"
```

### Adicione a chave pública ao ~/.ssh/authorized_keys no seu servidor.

### Adicione a chave privada aos segredos do GitHub:

- Vá para a página do repositório no GitHub.
- Clique em "Settings" > "Secrets and variables" > "Actions".
- Clique em "New repository secret".
- Adicione a chave privada como valor e nomeie como "SSH_PRIVATE_KEY".

### Os arquivos de Confuguração:

#### django.yml

```bash
name: Django CI/CD

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.12]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test

  web-deploy:
    name: Deploy
    runs-on: ubuntu-latest
    needs: build

    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Setup SSH
      run: |
        mkdir -p ~/.ssh
        echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
        chmod 600 ~/.ssh/id_rsa
        ssh-keyscan -H 35.239.14.1 >> ~/.ssh/known_hosts

    - name: List files in the current directory
      run: ls -l

    - name: Transfer deploy.sh to server
      run: |
        scp -o StrictHostKeyChecking=no deploy.sh renorb03@35.239.14.1:/home/renorb03/deploy.sh

    - name: Deploy to server
      run: |
        ssh -o StrictHostKeyChecking=no renorb03@35.239.14.1 'bash /home/renorb03/deploy.sh'

```
#### deploy.sh

```bash
cd /home/renorb03/bs-ecommerce
git pull origin main
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart bsloja
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
