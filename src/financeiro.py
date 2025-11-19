class Transacao:
    def __init__(self, descricao, valor, categoria):
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

def calcular_total(transacoes):
    total = 0
    for t in transacoes:
        total += t.valor
    return total