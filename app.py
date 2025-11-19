import streamlit as st
from src.financeiro import ContaFinanceira

# Configuração da Página
st.set_page_config(
    page_title="Sistema Financeiro",
    page_icon="💰",
    layout="centered"
)

# --- Título e Estilo ---
st.title("💰 Controle Financeiro Pessoal")
st.markdown("---")

# --- Gerenciamento de Estado (Memória do Site) ---
# O Streamlit recarrega a cada clique, então precisamos salvar a conta na "sessão"
if 'conta' not in st.session_state:
    # Cria a conta apenas na primeira vez que abre o site
    st.session_state.conta = ContaFinanceira("Minha Carteira")

conta = st.session_state.conta

# --- Sidebar (Lateral) para Ações ---
st.sidebar.header("Nova Operação")
tipo_operacao = st.sidebar.radio("O que você quer fazer?", ["Receita", "Despesa", "Investir/Render"])

with st.sidebar.form("form_operacao"):
    if tipo_operacao == "Receita":
        desc = st.text_input("Descrição (ex: Salário)")
        valor = st.number_input("Valor (R$)", min_value=0.01, step=10.0)
        submit = st.form_submit_button("🤑 Adicionar Receita")
        
        if submit:
            try:
                conta.adicionar_receita(desc, valor)
                st.success("Receita adicionada com sucesso!")
            except ValueError as e:
                st.error(f"Erro: {e}")

    elif tipo_operacao == "Despesa":
        desc = st.text_input("Descrição (ex: Aluguel)")
        valor = st.number_input("Valor (R$)", min_value=0.01, step=10.0)
        submit = st.form_submit_button("💸 Adicionar Despesa")
        
        if submit:
            try:
                conta.adicionar_despesa(desc, valor)
                st.success("Despesa lançada!")
            except ValueError as e:
                st.error(f"Erro: {e}")

    elif tipo_operacao == "Investir/Render":
        porc = st.number_input("Porcentagem de Rendimento (%)", min_value=0.1, step=0.1)
        submit = st.form_submit_button("📈 Aplicar Rendimento")
        
        if submit:
            try:
                conta.aplicar_rendimento(porc)
                st.success(f"Rendimento de {porc}% aplicado!")
            except ValueError as e:
                st.error(f"Erro: {e}")

# --- Área Principal (Dashboard) ---

# 1. Exibir Saldo Grande
col1, col2, col3 = st.columns(3)
col1.metric("Saldo Atual", f"R$ {conta.saldo:.2f}")
col2.metric("Total Receitas", f"R$ {conta.total_receitas():.2f}")
col3.metric("Total Despesas", f"R$ {conta.total_despesas():.2f}", delta_color="inverse")

st.markdown("---")

# 2. Tabela de Transações
st.subheader("📜 Extrato de Movimentações")

# Convertendo as transações para um formato que a tabela entenda fácil
if len(conta.transacoes) > 0:
    dados = []
    for t in conta.transacoes:
        dados.append({
            "Descrição": t.descricao,
            "Valor (R$)": f"{t.valor:.2f}",
            "Categoria": t.categoria,
            "Tipo": "Entrada" if t.valor > 0 else "Saída"
        })
    st.dataframe(dados, use_container_width=True)
else:
    st.info("Nenhuma transação registrada ainda.")

# Botão para limpar tudo (Reset)
if st.button("🗑️ Resetar Conta"):
    st.session_state.conta = ContaFinanceira("Minha Carteira")
    st.rerun()