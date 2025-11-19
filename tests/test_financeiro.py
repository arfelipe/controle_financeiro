import pytest
from src.financeiro import Transacao, calcular_total

# Teste 1: Verifica se cria transação corretamente
def test_criar_transacao_valida():
    t = Transacao("Salário", 1000.0, "Receita")
    assert t.valor == 1000.0
    assert t.descricao == "Salário"

# Teste 2: Verifica se impede valor negativo (Validação)
def test_criar_transacao_valor_negativo():
    with pytest.raises(ValueError):
        Transacao("Erro", -50, "Despesa")

# Teste 3: Verifica cálculo total
def test_calcular_total():
    t1 = Transacao("Luz", 100, "Despesa")
    t2 = Transacao("Água", 50, "Despesa")
    lista = [t1, t2]
    assert calcular_total(lista) == 150