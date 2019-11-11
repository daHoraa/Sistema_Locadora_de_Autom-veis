import sqlite3 as sql

class BdAccess():
    database    = "funcionarios.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        BdAccess.conn = sql.connect(BdAccess.database)
        BdAccess.cur = BdAccess.conn.cursor()
        BdAccess.connected = True

    def disconnect(self):
        BdAccess.conn.close()
        BdAccess.connected = False

    def execute(self, sql, parms = None):
        if BdAccess.connected:
            if parms == None:
                BdAccess.cur.execute(sql)
            else:
                BdAccess.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return BdAccess.cur.fetchall()
 
    def persist(self):
        if BdAccess.connected:
            BdAccess.conn.commit()
            return True
        else:
            return False

class ClientDAO:
    def __init__(self):
        "Quando a aplicação for executada pela primeira vez, cria-se o banco de dados"
        self.bd = BdAccess()
        self.bd.connect()
        self.bd.persist()

    def view(self):
        "recupera todos os dados do banco."
        rows = None
        try:
            self.bd.execute("SELECT * FROM clientes")    
            rows = self.bd.fetchall()
        except sql.Error as error:
            print("Falha ao tentar selecionar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
            raise sql.Error()
        return rows

    def insert(self, cliente):
        "insere novos registros no banco"
        try:
            self.bd.execute("INSERT INTO clientes VALUES(NULL, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"), ( self.nacionalidade , self.tipo_domumento , self.cpf , self.nome , self.sobrenome , self.email , self.cpf , self.genero , self.telefone, self.rg , self.nascimento , self.cep , self.logradouro , self.endereco , self.numero_endereco , self.complemento , self.bairro , self.cidade , self.estado))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar inserir os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
        