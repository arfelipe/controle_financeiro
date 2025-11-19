# Sistema de Controle Financeiro Pessoal

Este repositório contém o trabalho prático da disciplina de Teste de Software/Engenharia de Software. O objetivo principal é demonstrar a aplicação de testes automatizados e integração contínua (CI/CD) em um sistema de software.

## 👨‍🎓 Membros do Grupo

* **Arthur Felipe Ferreira** - Matrícula: 2019070000

---

## 📝 Sobre o Sistema

O sistema desenvolvido é um **Gerenciador Financeiro Pessoal**. Ele foi criado para permitir que o usuário controle suas finanças de forma simples e eficiente, garantindo a integridade dos cálculos através de validações rigorosas.

**Principais Funcionalidades:**
* **Gerenciar Transações:** Cadastro de Receitas e Despesas com descrições e categorias.
* **Visualizar Saldo:** O saldo é atualizado automaticamente a cada operação.
* **Investimentos:** Funcionalidade que aplica uma taxa de rendimento sobre o saldo atual.
* **Transferências:** Simulação de envio de valores entre contas.
* **Interface Web:** O sistema possui uma interface visual interativa construída com Streamlit.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Interface (Frontend):** Streamlit
* **Testes:** Pytest
* **Cobertura:** Pytest-Cov e Coverage.py
* **CI/CD:** GitHub Actions (Testes automáticos em Windows, Linux e MacOS)
* **Qualidade:** Codecov

---

## ⚙️ Instalação e Configuração

Antes de executar os testes ou a aplicação, prepare o ambiente:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/arfelipe/controle_financeiro.git](https://github.com/arfelipe/controle_financeiro.git)
   cd controle_financeiro
2. **Crie e ative o ambiente virtual:**

No Windows:


python -m venv venv
.\venv\Scripts\activate
No Linux/Mac:


python3 -m venv venv
source venv/bin/activate

3. **Instale as dependências:**

pip install -r requirements.txt

**🧪 Como Executar os Testes Localmente**
O projeto conta com 30 testes de unidade e 5 testes de integração. Para rodar a bateria de testes e verificar a cobertura do código, execute o comando abaixo no terminal:

python -m pytest --cov=src
Resultado Esperado: O terminal deve exibir a lista de testes com status "PASSED" (verde) e uma tabela indicando 100% de cobertura.

**💻 Como Rodar a Aplicação (Interface Web)**
Para utilizar o sistema através da interface gráfica no navegador, utilize o comando do Streamlit:

streamlit run app.py