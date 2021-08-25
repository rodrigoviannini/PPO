class ContaCorrente(object):
    # Similar ao carro temos um construtor com os atributos da conta corrente
    # além da definição da fatura que vem por padrão zerada (o underline do atributo sera explicado já já, não se preocupe)
    def __init__(self, titular, cpfTitular, saldo):
        self.titular = titular
        self.cpfTitular = cpfTitular
        self.saldo = saldo
        self.limite = 1000
        
contaDoBrian = ContaCorrente("Brian Nunes", "123456789-50", 1000000000)

print(contaDoBrian.titular)
print(contaDoBrian.cpfTitular)
print(contaDoBrian.saldo)
print(contaDoBrian.limite)