# Agendador de Salas

Sistema de gerenciamento de reservas desenvolvido como exercício.


## Funcionalidades Implementadas

- **Validação Temporal Robusta:** Algoritmo que impede conflitos de horário (incluindo sobreposições parciais).
- **Busca e Filtros:** Pesquisa dinâmica por nome da sala ou capacidade mínima.
- **Autenticação Customizada:** Sistema de login/logout integrado (sem depender apenas do Django Admin).
- **Controle de Acesso:**
  - Usuários comuns: Visualizam e gerenciam apenas suas próprias reservas.
  - Staff/Admin: Cadastram novas salas e gerenciam todo o sistema.
- **Interface Responsiva:** Layout adaptado para mobile e desktop.


## Instalação e Configuração

Siga estes passos para rodar o projeto em uma nova máquina (Windows, Linux ou WSL).

### Pré-requisitos
- Python 3.10 ou superior.
- Git instalado.

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/rafael-hc/agendador.git
   cd agendador
   ```

2.  **Crie e ative o Ambiente Virtual**

    *Linux / WSL:*

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    *Windows (PowerShell):*

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

3.  **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare o Banco de Dados**

    ```bash
    python manage.py migrate
    ```

5.  **Crie um Usuário Administrador**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o Servidor**

    ```bash
    python manage.py runserver
    ```

    Acesse: `http://127.0.0.1:8000/`

## Testes Automatizados

O projeto possui cobertura de testes unitários para garantir a integridade das regras de negócio (especialmente a validação de conflitos).

Para executar os testes:

```bash
python manage.py test reservas
```

-----

**Desenvolvido por Rafael Carneiro**
