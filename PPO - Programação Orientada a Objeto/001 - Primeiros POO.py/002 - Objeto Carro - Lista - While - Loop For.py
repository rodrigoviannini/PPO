class Carro(object):
    """
        Este aqui é o método do contrutor! Ele sempre tem esse nome.
        Aqui nosso construtor recebe uma referência para o objeto que está contruindo: 'self'
        e todos os estados que serão atribuidos aos atributos.
    """
    def __init__(self, cor, ano, estado, velocidade):
        self.cor = cor
        self.ano = ano
        self.estado = estado
        self.velocidade = velocidade
        
listaCarros = []
cadastrar = "s"
while cadastrar =="s":
    corDoUsuario = input("Digite a cor: ")
    anoDoUsuario = input("Digite a ano: ")
    estadoDoUsuario = input("Digite a estado: ")
    velocidadeDoUsuario = input("Digite a velocidade: ")
    
    listaCarros.append(Carro(corDoUsuario, anoDoUsuario, estadoDoUsuario, velocidadeDoUsuario))
    
    cadastrar = input("Quer cadastrar mais carros?")

# EXEMPLO DE SOLICITAÇÃO DE CARATERÍSITCA DE UM UNICO ITEM -> ATRIBUTOS
for idx, carro in enumerate(listaCarros):
    print(idx, carro.cor)
    print(idx, carro.ano)
    print(idx, carro.estado)
    print(idx, carro.velocidade)
    print()

# PINTANDO TODOS OS CARROS DE PRATA
for carro in listaCarros: # IMPRIME TODAS AS CORES DOS CARROS
    print(carro.cor)

print()
print("Printando todos os carros....")
print()

for carro in listaCarros:
    carro.cor = "Prata" # PINTA TODOS OS CARROS DE PRATA

for carro in listaCarros: # IMPRIME TODAS AS CORES DOS CARROS
    print(carro.cor)