import pytest
from src.financeiro import ContaFinanceira, Transacao

# --- GRUPO 1: Testes de Inicialização e Transação (3 testes) ---
def test_criar_conta_com_saldo_inicial():
    conta = ContaFinanceira("Minha Conta", 100.0)
    assert conta.saldo == 100.0
    assert conta.nome == "Minha Conta"

def test_criar_conta_saldo_padrao_zero():
    conta = ContaFinanceira("Conta Zerada")
    assert conta.saldo == 0.0

def test_criar_transacao_descricao_vazia_erro():
    with pytest.raises(ValueError):
        Transacao("", 100, "Teste")

# --- GRUPO 2: Adicionar Receitas (3 testes) ---
def test_adicionar_receita_aumenta_saldo():
    conta = ContaFinanceira("Teste")
    conta.adicionar_receita("Salário", 1000.0)
    assert conta.saldo == 1000.0

def test_receita_valor_negativo_erro():
    conta = ContaFinanceira("Teste")
    with pytest.raises(ValueError):
        conta.adicionar_receita("Erro", -100)

def test_receita_valor_zero_erro():
    conta = ContaFinanceira("Teste")
    with pytest.raises(ValueError):
        conta.adicionar_receita("Erro", 0)

# --- GRUPO 3: Adicionar Despesas (4 testes) ---
def test_adicionar_despesa_diminui_saldo():
    conta = ContaFinanceira("Teste", 500.0)
    conta.adicionar_despesa("Luz", 100.0)
    assert conta.saldo == 400.0

def test_adicionar_multiplas_despesas():
    conta = ContaFinanceira("Teste", 100.0)
    conta.adicionar_despesa("Gás", 30)
    conta.adicionar_despesa("Água", 20)
    assert conta.saldo == 50.0

def test_despesa_gera_transacao_negativa():
    conta = ContaFinanceira("Teste")
    conta.adicionar_despesa("Teste", 50)
    transacao = conta.transacoes[0]
    assert transacao.valor == -50

def test_despesa_valor_negativo_erro():
    conta = ContaFinanceira("Teste")
    with pytest.raises(ValueError):
        conta.adicionar_despesa("Erro", -50)

# --- GRUPO 4: Filtragem e Listagem (5 testes) ---
def test_listar_transacoes_retorna_todas():
    conta = ContaFinanceira("Teste")
    conta.adicionar_receita("A", 10)
    conta.adicionar_despesa("B", 5)
    assert len(conta.listar_transacoes()) == 2

def test_listar_por_categoria_existente():
    conta = ContaFinanceira("Teste")
    conta.adicionar_receita("Salário", 1000, "Trabalho")
    conta.adicionar_receita("Freela", 500, "Extra")
    filtrado = conta.listar_por_categoria("Trabalho")
    assert len(filtrado) == 1
    assert filtrado[0].descricao == "Salário"

def test_listar_por_categoria_inexistente():
    conta = ContaFinanceira("Teste")
    conta.adicionar_receita("A", 10, "X")
    assert conta.listar_por_categoria("Y") == []

def test_total_receitas_correto():
    conta = ContaFinanceira("Teste")
    conta.adicionar_receita("A", 100)
    conta.adicionar_receita("B", 50)
    conta.adicionar_despesa("C", 20) # Não deve somar
    assert conta.total_receitas() == 150

def test_total_despesas_correto():
    conta = ContaFinanceira("Teste")
    conta.adicionar_despesa("A", 50) # -50
    conta.adicionar_despesa("B", 20) # -20
    conta.adicionar_receita("C", 100) # Não deve somar
    assert conta.total_despesas() == -70

# --- GRUPO 5: Rendimentos (5 testes) ---
def test_aplicar_rendimento_aumenta_saldo():
    conta = ContaFinanceira("Inv", 100.0)
    conta.aplicar_rendimento(10) # 10% de 100 = 10
    assert conta.saldo == 110.0

def test_aplicar_rendimento_gera_transacao():
    conta = ContaFinanceira("Inv", 100.0)
    conta.aplicar_rendimento(10)
    ultima = conta.transacoes[-1]
    assert ultima.categoria == "Investimento"
    assert ultima.valor == 10.0

def test_aplicar_rendimento_zero_porcento():
    conta = ContaFinanceira("Inv", 100.0)
    conta.aplicar_rendimento(0)
    assert conta.saldo == 100.0

def test_rendimento_negativo_erro():
    conta = ContaFinanceira("Inv")
    with pytest.raises(ValueError):
        conta.aplicar_rendimento(-5)

def test_rendimento_sobre_saldo_zerado():
    conta = ContaFinanceira("Inv", 0.0)
    conta.aplicar_rendimento(10)
    assert conta.saldo == 0.0

# --- GRUPO 6: Transferências entre Contas (10 testes para fechar 30) ---
def test_transferencia_diminui_origem():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    origem.transferir_para(destino, 50)
    assert origem.saldo == 50

def test_transferencia_aumenta_destino():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    origem.transferir_para(destino, 50)
    assert destino.saldo == 50

def test_transferencia_sem_saldo_erro():
    origem = ContaFinanceira("A", 10)
    destino = ContaFinanceira("B", 0)
    with pytest.raises(ValueError):
        origem.transferir_para(destino, 50)

def test_transferencia_valor_negativo_erro():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    with pytest.raises(ValueError):
        origem.transferir_para(destino, -10)

def test_transferencia_gera_despesa_na_origem():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    origem.transferir_para(destino, 50)
    t = origem.transacoes[-1]
    assert t.categoria == "Transferência"
    assert t.valor == -50

def test_transferencia_gera_receita_no_destino():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    origem.transferir_para(destino, 50)
    t = destino.transacoes[-1]
    assert t.categoria == "Transferência"
    assert t.valor == 50

def test_transferencia_exata_do_saldo():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    origem.transferir_para(destino, 100) # Zera a conta
    assert origem.saldo == 0

def test_transferencia_valor_zero_erro():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    with pytest.raises(ValueError):
        origem.transferir_para(destino, 0)

def test_multiplas_transferencias():
    origem = ContaFinanceira("A", 100)
    destino = ContaFinanceira("B", 0)
    origem.transferir_para(destino, 20)
    origem.transferir_para(destino, 20)
    assert origem.saldo == 60
    assert destino.saldo == 40

def test_saldo_apos_receita_e_transferencia():
    origem = ContaFinanceira("A", 0)
    destino = ContaFinanceira("B", 0)
    origem.adicionar_receita("Salario", 1000)
    origem.transferir_para(destino, 500)
    assert origem.saldo == 500