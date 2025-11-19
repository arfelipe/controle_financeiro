from src.financeiro import ContaFinanceira

# Cenario 1: Ciclo Mensal Completo
def test_fluxo_mensal_completo():
    conta = ContaFinanceira("Arthur")
    # 1. Recebe Salário
    conta.adicionar_receita("Salário", 5000.0, "Renda")
    # 2. Paga Contas Essenciais
    conta.adicionar_despesa("Aluguel", 1500.0, "Moradia")
    conta.adicionar_despesa("Luz", 150.0, "Contas")
    conta.adicionar_despesa("Internet", 100.0, "Contas")
    # 3. Investe uma parte
    conta.aplicar_rendimento(10) # Digamos que rendeu 10% sobre o saldo atual (3250) -> +325
    
    # Validação Final
    # Saldo esperado: 5000 - 1500 - 150 - 100 + 325 = 3575
    assert conta.saldo == 3575.0
    assert len(conta.transacoes) == 5

# Cenario 2: Transferência entre Familiares
def test_fluxo_transferencia_familia():
    pai = ContaFinanceira("Pai", 1000.0)
    filho = ContaFinanceira("Filho", 0.0)
    
    # Pai paga mesada
    pai.transferir_para(filho, 200.0)
    
    # Filho gasta mesada
    filho.adicionar_despesa("Cinema", 50.0, "Lazer")
    filho.adicionar_despesa("Lanche", 30.0, "Lazer")
    
    assert pai.saldo == 800.0
    assert filho.saldo == 120.0

# Cenario 3: Gestão de Orçamento Apertado (Fail-Safe)
def test_fluxo_orcamento_apertado():
    conta = ContaFinanceira("Estudante", 100.0)
    
    # Tenta gastar mais do que tem (deve falhar mas não quebrar o sistema)
    try:
        conta.transferir_para(ContaFinanceira("Loja"), 200.0)
    except ValueError:
        pass # Erro esperado e tratado
        
    # Gasta valor permitido
    conta.adicionar_despesa("Livro", 80.0, "Educação")
    
    assert conta.saldo == 20.0

# Cenario 4: Auditoria de Categorias
def test_fluxo_auditoria():
    conta = ContaFinanceira("Empresa")
    conta.adicionar_receita("Venda A", 1000, "Vendas")
    conta.adicionar_receita("Venda B", 2000, "Vendas")
    conta.adicionar_despesa("Imposto", 500, "Impostos")
    
    vendas = conta.listar_por_categoria("Vendas")
    total_vendas = sum(t.valor for t in vendas)
    
    assert len(vendas) == 2
    assert total_vendas == 3000

# Cenario 5: Rendimento Composto Simulado
def test_fluxo_rendimento_composto():
    conta = ContaFinanceira("Poupança", 1000.0)
    
    # Mês 1
    conta.aplicar_rendimento(10) # +100 -> 1100
    # Mês 2
    conta.aplicar_rendimento(10) # +110 -> 1210
    
    assert conta.saldo == 1210.0