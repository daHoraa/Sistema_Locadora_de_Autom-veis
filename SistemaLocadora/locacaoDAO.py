from dao import DataBaseAccess, sqlite3
from locacao import Locacao

class LocacaoDAO:
    def __init__(self):
        '''Se conecta ao banco de dados'''
        self.database = DataBaseAccess()
        self.database.connect()
        self.database.persist()

    def view(self):
        resultado = None
        try:
            self.database.execute('SELECT * FROM locacao')
            resultado = self.database.fetchall()
        except sqlite3.Error:
            print('Falha ao tentar selecionar os registros.')
        return resultado

    def insert(self, locacao):
        '''Insere as locacao no banco de dados'''
        try:
            self.database.execute("INSERT INTO locacao(id_cliente, id_veiculo, data_inicial, diarias, valor_locacao) VALUES(?,?,?,?,?)", 
            (locacao.id_cliente, locacao.id_veiculo, locacao.data_inicial, locacao.diarias, locacao.valor_locacao))
            self.database.persist()
        except sqlite3.Error:
            print("Falha ao tentar inserir no banco de dados.")


    def update(self, locacao, id):
        '''Irá atualizar os registros no banco de dados'''
        try:
            self.database.execute("UPDATE locacao SET id_cliente=?, id_veiculo=?, data_inicial=?, diarias=?, valor_locacao=? WHERE id=?", (locacao.id_cliente, locacao.id_veiculo, locacao.data_inicial, locacao.diarias, locacao.valor_locacao, id))
            self.database.persist()
        except sqlite3.Error:
            print("Falha ao tentar inserir.")


    def delete(self, id):
        "Deleta as locacao do bando de dados"
        try:
            self.database.execute("DELETE FROM locacao WHERE id=?", (id,))
            self.database.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar remover o registro")
            print("Classe de exceção: ", error.__class__)
            print("Exceção é ", error.args)


    def close(self):
        '''Fechando conexão com o banco de dados.'''
        self.database.disconnect()