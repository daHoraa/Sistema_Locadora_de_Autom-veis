from dao import DataBaseAccess, sqlite3
from veiculo import Veiculo


class VeiculoDAO:
    def __init__(self):
        '''Se conecta ao banco de dados'''
        self.database = DataBaseAccess()
        self.database.connect()
        self.database.persist()

    def view(self):
        resultado = None
        try:
            self.database.execute('SELECT * FROM veiculos')
            resultado = self.database.fetchall()
        except sqlite3.Error:
            print('Falha ao tentar selecionar os registros.')
        return resultado

    def insert(self, veiculo):
        '''Insere novos registros no Banco de Dados.'''
        try:
            self.database.execute('INSERT INTO veiculos(marca, modelo, ano, cor, tanque, combustivel, consumo_cidade, consumo_estrada, tempo_0_100, chassi, placa, tamanho_pneu, som, valor_diaria) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.cor, veiculo.tanque, veiculo.combustivel, veiculo.consumo_cidade, veiculo.consumo_estrada, veiculo.tempo_0_100, veiculo.chassi, veiculo.placa, veiculo.tamanho_pneu, veiculo.som, veiculo.valor_diaria))
            self.database.persist()
        except sqlite3.Error:
            print('Falha ao tentar inserir registros na tabela veiculo.')

    def update(self, veiculo, id):
        '''Atualiza os registros no Banco de Dados.'''
        try:
            self.database.execute('UPDATE veiculos SET marca =?, modelo=?, ano=?, cor=?, tanque =?, combustivel =?, consumo_cidade =?, consumo_estrada =?, tempo_0_100 =?, chassi =?, placa =?, tamanho_pneu =?, som =?, valor_diaria =? WHERE id = ?', (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.cor,veiculo.tanque, veiculo.combustivel, veiculo.consumo_cidade, veiculo.consumo_estrada, veiculo.tempo_0_100, veiculo.chassi, veiculo.placa, veiculo.tamanho_pneu,veiculo.som, veiculo.valor_diaria, id))
            self.database.persist()
        except sqlite3.Error:
            print('Falha ao tentar inserir registros na tabela veiculo.')

    def delete(self, id):
        "Deleta os registros do banco de dados."
        try:
            self.database.execute("DELETE FROM veiculos WHERE id = ?", (id,))
            self.database.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar remover o registro")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def close(self):
        '''Fechando conexão com o banco de dados.'''
        self.database.disconnect()
