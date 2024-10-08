# TicketGo

TicketGo é um marketplace de ingressos online que permite aos usuários comprar e vender ingressos de forma simples e segura.

## Principais Funcionalidades:
- Integração com Asaas: <br/>
  Facilita o processamento de pagamentos, garantindo transações seguras e confiáveis.

- Backup de Dados: <br/>
  Possui um comando para backup, assegurando a integridade e a recuperação de informações críticas.

- Auditoria de Mudanças: <br/>
  Implementa auditoria usando django-simple-history, permitindo rastrear alterações em usuários e compras.

- Autenticação via Token: <br/>
  Garante segurança na autenticação de usuários, permitindo acesso controlado aos recursos da API.

## Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### Clonar o Repositório

```
git clone https://github.com/seu-usuario/apps.git
cd apps
```

### Criar e Ativar um Ambiente Virtual

```
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

### Instalar as Dependências

```
pip install -r requirements.txt
```

### Copiar .env-EXAMPLE to .env

### Alterar .env conforme necessário

### Criar e conectar um banco de dados PostgreSQL

```
pip install -r requirements.txt
```

## Aplicar migrações

```
python manage.py migrate
```

## Após realizar as migrações, Carregue os dados fictícios

```
python manage.py loaddata initial_data.json
```

### Criar superusuário

```
python manage.py createsuperuser
```

### Fazer backup do banco de dados

```
python manage.py backupdb
```

### Rodar o Servidor de Desenvolvimento

```
python manage.py runserver
```
