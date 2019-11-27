
class Locacao():
    def __init__(self, id_cliente="", id_veiculo="", data_inicial="", data_final="", diarias="", valor_locacao=""):
        # dados da cnh
        self.id_cliente = id_cliente
        self.id_veiculo = id_veiculo
        self.data_inicial = data_inicial
        self.diarias = diarias
        self.valor_locacao = valor_locacao
