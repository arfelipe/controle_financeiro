class Transacao:
    def __init__(self, descricao, valor, categoria):
        if not descricao:
            raise ValueError("A descrição não pode ser vazia.")
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

class ContaFinanceira:
    def __init__(self, nome, saldo_inicial=0.0):
        self.nome = nome
        self.saldo = saldo_inicial
        self.transacoes = []

    def adicionar_receita(self, descricao, valor, categoria="Receita"):
        if valor <= 0:
            raise ValueError("O valor da receita deve ser positivo.")
        nova_transacao = Transacao(descricao, valor, categoria)
        self.transacoes.append(nova_transacao)
        self.saldo += valor

    def adicionar_despesa(self, descricao, valor, categoria="Despesa"):
        if valor <= 0:
            raise ValueError("O valor da despesa deve ser positivo.")
        # Despesas subtraem do saldo, então armazenamos como negativo ou tratamos na subtração
        # Aqui vamos armazenar negativo para facilitar a soma
        nova_transacao = Transacao(descricao, -valor, categoria)
        self.transacoes.append(nova_transacao)
        self.saldo -= valor

    def listar_transacoes(self):
        return self.transacoes

    def listar_por_categoria(self, categoria):
        return [t for t in self.transacoes if t.categoria == categoria]

    def total_receitas(self):
        return sum(t.valor for t in self.transacoes if t.valor > 0)

    def total_despesas(self):
        return sum(t.valor for t in self.transacoes if t.valor < 0)

    def aplicar_rendimento(self, porcentagem):
        if porcentagem < 0:
            raise ValueError("O rendimento não pode ser negativo.")
        
        rendimento = self.saldo * (porcentagem / 100)
        
        # CORREÇÃO: Só adiciona receita se houver rendimento real (maior que zero)
        if rendimento > 0:
            self.adicionar_receita("Rendimento Automático", rendimento, "Investimento")

    def transferir_para(self, conta_destino, valor):
        if valor <= 0:
            raise ValueError("Valor de transferência inválido.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para transferência.")
        
        self.adicionar_despesa(f"Transferência para {conta_destino.nome}", valor, "Transferência")
        conta_destino.adicionar_receita(f"Transferência de {self.nome}", valor, "Transferência")