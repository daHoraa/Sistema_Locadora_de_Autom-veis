class Veiculo:
    def __init__(self, marca="", modelo="", ano="", cor="",tanque="",combustivel="",consumo_cidade="",consumo_estrada="",tempo_0_100="",chassi="",placa="",tamanho_pneu="",
    som="",valor_diaria=""):
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

    def __str__(self):
        print(self.marca, self.modelo, self.ano, self.cor,self.tanque,self.combustivel,self.consumo_cidade,self.consumo_estrada, self.tempo_0_100,self.chassi,self.placa, self.tamanho_pneu,self.som,self.valor_diaria)
