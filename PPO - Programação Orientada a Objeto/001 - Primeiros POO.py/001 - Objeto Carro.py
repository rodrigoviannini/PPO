# Esse parâmetro object será melhor abordado já já quando falarmos de herança
class Carro(object): # CLASSE == PLANTA
    """
        Este aqui é o método do contrutor! Ele sempre tem esse nome.
        Aqui nosso construtor recebe uma referência para o objeto que está contruindo: 'self'
        e todos os estados que serão atribuidos aos atributos.
    """
    def __init__(self, cor, ano, estado, velocidade): # CONSTRUTOR
        self.cor = cor
        self.ano = ano
        self.estado = estado
        self.velocidade = velocidade
        
    # O método acelerar nos permite aumentar a velocidade do carro baseado em uma aceleração e o tempo que ela é aplicada 
    def acelerar(self, aceleracao, tempo): # MÉTODO -> Usar o verbo!
        self.velocidade += aceleracao * tempo
        
    # O método frear nos permite diminuir a velocidade do carro baseado em uma desaceleração e o tempo que ela é aplicada 
    def frear(self, desaceleracao, tempo): # MÉTODO -> Usar o verbo!
        self.velocidade -= desaceleracao * tempo
        
    # O método pintar altera a cor do carro a partir da cor recebida nos parâmetros.
    def pintar(self, novaCor): # MÉTODO -> Usar o verbo!
        self.cor = novaCor
        
""" 
    Aqui estamos instanciando o objeto carro
    Repare que chamamos a classe semelhante a uma função, e passamos os atributos que serão utilizados no construtor
    Isso se deve pois estamos chamando o contrutor de uma classe para "construir" o nosso carro da maneira que pedimos
"""

fiesta = Carro('Vermelho', 2017, 'Novo', 0)

# Exemplos de uso dos métodos

# Podemos nos referir aos atributos de um objeto com o nome dele seguido de um ponto e o atributo desejado:

print('Cor: ', fiesta.cor)
print('Ano: ', fiesta.ano)
print('Velocidade: ', fiesta.velocidade)

print('\nAcelerando fiesta 2m/s^2 por 5 segundos...\n')
fiesta.acelerar(2, 5) # CHAMANDO O MÉTODO

print('Nova velocidade: ', fiesta.velocidade)

# Note que podemos acrescentar atributos por fora da classe de maneira dinâmica
fiesta.seguro  = True
print(fiesta.seguro)