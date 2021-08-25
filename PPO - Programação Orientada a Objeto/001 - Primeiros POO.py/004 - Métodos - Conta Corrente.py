class contaCorrente(object):
    # Similar ao carro temos um construtor com os atributos da conta corrente
    # além da definição da fatura que vem por padrão zerada (o underline do atributo sera explicado já já, não se preocupe)
    def __init__(self, saldo, titular, limite):
        self.saldo = saldo
        self.titular = titular
        self.limite = limite
        self._fatura = 0
        
    # O método gastar retira valores do saldo a medida do possivel (que não negative a conta)
    def gastar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')
        
    # O método ganhar acrescenta valor ao saldo
    def ganhar(self, valor):
        self.saldo += valor
        
    # Esse método irá aumentar a fatura, mas antes irá conferir se o limite permite a operação
    def gastarCredito(self, valor):
        if((self._fatura + valor) <= self.limite):
            self._fatura += valor
        else:
            print('Esta compra está acima do seu limite de compra.')
       
    # O método pagaFatura diminui a fatura a medidade que o saldo permite e o cliente quer
    def pagaFatura(self, valor):
        if(self.saldo >= valor):
            if(0 >= self._fatura - valor):
                self._fatura -= valor;
                self.saldo -= valor;
            else:
                print('Este valor está acima da sua fatura de:', self._fatura)
        else:
            print('Você não possui saldo para esta operação')

    #getter da fatura (isso será exeplicado junto com o underline do atributo, está tudo em ordem por aqui!)
    @property
    def fatura(self):
        return self._fatura

# Instanciamos a conta com os atributos exemplos
conta = contaCorrente(1000000, 'Brian Andrade Nunes', 10000)

# Exemplos de uso dos métodos

print('Saldo:', conta.saldo)
print('Comprando carrão novo...')
conta.gastar(350000)
print('Novo saldo:', conta.saldo)
print()
print('Fatura:', conta.fatura, ' | Limite:', conta.limite)
print('Estourando o cartão com R$15.000...')
conta.gastarCredito(15000)
print('Tirando alguns itens do carrinho e gastando apenas R$7.500...')
conta.gastarCredito(7500)
print('Nova fatura:', conta.fatura, ' | Limite:', conta.limite)