# ⚽ Bolão da Copa 2026

Aplicação web para gerenciar bolões da Copa do Mundo entre amigos e família. Cada participante pode dar seu palpite nos jogos pelo celular ou computador, sem precisar de papel!

## Funcionalidades

- Cadastro e login de usuários
- Criação de grupos (bolões) com código de convite
- Entrada em grupos através de código
- Palpites nos jogos da Copa do Mundo
- Edição de palpites (apenas antes do jogo começar)
- Dashboard administrativo com estatísticas
- Sincronização automática dos jogos via API

## Tecnologias

- **Backend:** Python 3 + Django
- **Banco de dados:** SQLite
- **Frontend:** Bootstrap 5
- **API de jogos:** [football-data.org](https://www.football-data.org/)

## Pré-requisitos

- Python 3.10+
- Chave de API do [football-data.org](https://www.football-data.org/) (plano gratuito)

## Como executar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd bolao
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
SECRET_KEY=sua_secret_key_aqui
DEBUG=True
FOOTBALL_API_KEY=sua_chave_aqui
```

Para gerar uma `SECRET_KEY`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Execute as migrations

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Sincronize os jogos da Copa

```bash
python manage.py sync_matches
```

### 8. Execute o servidor

```bash
python manage.py runserver
```

Acesse [http://localhost:8000](http://localhost:8000) no navegador.

## Estrutura do projeto

```
bolao/
  accounts/   # Autenticação e usuários
  groups/     # Grupos (bolões) e memberships
  matches/    # Jogos da Copa do Mundo
  guesses/    # Palpites dos usuários
  core/       # Página inicial e dashboard
  app/        # Configurações do projeto
  templates/  # Templates HTML globais
```

## Permissões

Apenas usuários com permissão de **staff** podem criar, editar e excluir grupos. Para dar essa permissão, acesse o painel admin em `/admin/` e edite o usuário desejado.

## Testes

```bash
python manage.py test
```