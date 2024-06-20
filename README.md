Makaan Real Estate Brokerage - User Management System
Description

Makaan Real Estate Brokerage User Management System is a practical fictitious project developed to manage user authentication, registration, and profile management for a real estate brokerage firm. It provides a streamlined web application where users can securely register, log in, update their profiles, and receive email notifications for important actions.
Features

    User Registration: Secure registration process with password strength validation.
    Login System: Reliable login system with authentication checks.
    Profile Management: Allows users to update personal information and profile images.
    Password Security: Utilizes Django's hashing mechanisms for secure password storage.
    Email Notifications: Sends emails for registration confirmation and profile updates.

Installation

To install and run the Makaan project locally:

    Clone the Repository:

    bash

git clone <repository_url>
cd makaan-project

Set Up Virtual Environment:

    Create a virtual environment:

    bash

python -m venv env

Activate the virtual environment:

    Windows:

    bash

.\env\Scripts\activate

macOS/Linux:

bash

        source env/bin/activate

Install Dependencies:

    pip install -r requirements.txt

Configuration

Before running the application:

    Database Setup:
        Configure database settings in settings.py.

    Email Configuration:
        Set up SMTP settings in settings.py for email notifications.

Usage

    Run the Application:

    python manage.py runserver

    Access the Application:
        Open a web browser and go to http://localhost:8000.
        Register a new account or log in with existing credentials.
        Update your profile details and upload a profile picture.

    Email Notifications:
        Upon registration, you will receive a welcome email.
        When you update your profile, you will receive a notification email confirming the update.

Contribution

Contributions to improve the Makaan Real Estate Brokerage User Management System are welcome. To contribute:

    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature).
    Commit your changes (git commit -am 'Add some feature').
    Push to the branch (git push origin feature/your-feature).
    Create a new Pull Request.

License

This project is licensed under the MIT License.






Sistema de Gerenciamento de Usuários da Corretora de Imóveis Makaan

Descrição

O Sistema de Gerenciamento de Usuários da Corretora de Imóveis Makaan é um projeto prático fictício desenvolvido para gerenciar autenticação de usuários, registro e gestão de perfis para uma corretora de imóveis. Ele fornece uma aplicação web simplificada onde os usuários podem se registrar de forma segura, fazer login, atualizar seus perfis e receber notificações por email para ações importantes.
Funcionalidades

    Registro de Usuário: Processo de registro seguro com validação de força de senha.
    Sistema de Login: Sistema de login confiável com verificações de autenticação.
    Gerenciamento de Perfil: Permite aos usuários atualizar informações pessoais e imagens de perfil.
    Segurança de Senha: Utiliza mecanismos de hash do Django para armazenamento seguro de senhas.
    Notificações por Email: Envia emails para confirmação de registro e atualizações de perfil.

Instalação

Para instalar e executar o projeto Makaan localmente:

    Clone o Repositório:

    bash

git clone <repository_url>
cd makaan-project

Configurar Ambiente Virtual:

    Crie um ambiente virtual:

    bash

python -m venv env

Ative o ambiente virtual:

    Windows:

    bash

.\env\Scripts\activate

macOS/Linux:

bash

        source env/bin/activate

Instalar Dependências:

    pip install -r requirements.txt

Configuração

Antes de executar a aplicação:

    Configuração do Banco de Dados:
        Configure as definições do banco de dados em settings.py.

    Configuração de Email:
        Configure as configurações SMTP em settings.py para notificações por email.

Uso

    Executar a Aplicação:

    python manage.py runserver

    Acessar a Aplicação:
        Abra um navegador da web e vá para http://localhost:8000.
        Registre uma nova conta ou faça login com credenciais existentes.
        Atualize os detalhes do seu perfil e faça upload de uma imagem de perfil.

    Notificações por Email:
        Após o registro, você receberá um email de boas-vindas.
        Quando você atualizar seu perfil, receberá um email de notificação confirmando a atualização.

Contribuição

Contribuições para melhorar o Sistema de Gerenciamento de Usuários da Corretora de Imóveis Makaan são bem-vindas. Para contribuir:

    Faça um fork do repositório.
    Crie um novo branch (git checkout -b feature/sua-feature).
    Faça commit das suas mudanças (git commit -am 'Adicionar alguma feature').
    Envie o código para o branch (git push origin feature/sua-feature).
    Crie um novo Pull Request.

Licença

Este projeto está licenciado sob a Licença MIT.
