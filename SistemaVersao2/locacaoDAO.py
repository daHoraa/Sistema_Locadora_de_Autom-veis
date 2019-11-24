from dao import DataBaseAccess, sqlite3
from veiculo import Veiculo


class LocacaoDAO:
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

    def close(self):
        '''Fechando conexão com o banco de dados.'''
        self.database.disconnect()