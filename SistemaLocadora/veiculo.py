
class Veiculo:
    '''Classe que representa um veiculo'''

    def __init__(self, marca='', modelo='', ano='', cor='', tanque='', combustivel='', consumo_cidade='', consumo_estrada='', tempo_0_100='', chassi='', placa='', tamanho_pneu='', som='', valor_diaria=''):
       ''' Inicializa um veiculo e recebe seus dados'''
       self.marca = marca
       self.modelo = modelo
       self.ano = ano
       self.cor = cor
       self.tanque = tanque
       self.combustivel = combustivel
       self.consumo_cidade = consumo_cidade
       self.consumo_estrada = consumo_estrada
       self.tempo_0_100 = tempo_0_100
       self.chassi = chassi
       self.placa = placa
       self.tamanho_pneu = tamanho_pneu        
       self.som = som
       self.valor_diaria = valor_diaria

