# Agendador de Salas - IFF

Sistema de gerenciamento de reservas de salas e laboratórios desenvolvido como Prova de Conceito (PoC) para otimizar o uso de espaços no campus do IFF.

O objetivo é substituir o controle manual/planilhas por uma solução centralizada que valida conflitos de horário automaticamente e permite autogestão pelos servidores.

## 🚀 Tecnologias Utilizadas

- **Backend:** Python 3.10+ / Django 5.x
- **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsivo)
- **Banco de Dados:** SQLite (Ambiente de Desenvolvimento)
- **Controle de Versão:** Git / GitHub

## 📋 Funcionalidades Principais

- **Busca Inteligente:** Filtragem de salas por nome ou capacidade mínima.
- **Validação de Conflitos:** Lógica robusta que impede matematicamente o choque de horários (incluindo sobreposições parciais).
- **Gestão de Reservas:** Painel "Minhas Reservas" onde o usuário visualiza e cancela seus agendamentos.
- **Segurança:** Sistema de permissões onde apenas o dono da reserva pode cancelá-la.
- **Interface Amigável:** Layout limpo e responsivo utilizando Bootstrap.

## 🔧 Instalação e Configuração

Siga estes passos para rodar o projeto em uma nova máquina (Windows, Linux ou WSL).

### Pré-requisitos
- Python 3.10 ou superior.
- Git instalado.

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/SEU_USUARIO_AQUI/agendador.git](https://github.com/SEU_USUARIO_AQUI/agendador.git)
   cd agendador
````

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

## ✅ Testes Automatizados

O projeto possui cobertura de testes unitários para garantir a integridade das regras de negócio (especialmente a validação de conflitos).

Para executar os testes:

```bash
python manage.py test reservas
```

-----

**Desenvolvido por Rafael Carneiro** | Técnico em Tecnologia da Informação - IFF
