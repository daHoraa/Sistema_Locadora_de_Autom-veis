import sqlite3 as sql
 
'''
* Para esta aplicação, precisamos apenas de uma tabela 
(que se chamará veiculos), com os seguintes campos:
    * Marca
    * Modelo
    * Ano
    * Cor
    * Tanque

'''

class BdAccess():
    database    = "veiculos.db"
    conn        = None
    cur         = None
    connected   = False
 
    def connect(self):
        "realiza conexão com o banco de dados"
        try:
            BdAccess.conn = sql.connect(BdAccess.database)
            BdAccess.cur = BdAccess.conn.cursor()
            BdAccess.connected = True
            self.execute("CREATE TABLE IF NOT EXISTS veiculos (id INTEGER PRIMARY KEY , marca TEXT, modelo TEXT, ano TEXT, cor TEXT, tanque TEXT, combustivel TEXT, consumo_cidade TEXT, consumo_estrada TEXT,tempo_0_100 TEXT, chassi TEXT, placa TEXT, tamanho_pneu TEXT, som TEXT, valor_diaria TEXT)")
        except sqlite3.Error as error:
            print("Erro no banco de dados: ", error)
 
    def disconnect(self):
        " fecha a conexão com o banco de dados"
        BdAccess.conn.close()
        BdAccess.connected = False
 
    def execute(self, sql, parms = None):
        '''
        executa um comando no banco de dados. recebe três parâmetros:
        * self: referencia para o próprio objeto. não precisa ser informado;
        * sql: comando SQL a ser executado;
        * parms: vetor com os parâmetros do comando SQL. Pode ser omitido.
        '''
        if BdAccess.connected:
            if parms == None:
                BdAccess.cur.execute(sql)
            else:
                BdAccess.cur.execute(sql, parms)
            return True
        else:
            return False
 
    def fetchall(self):
        "recupera os valores recebidos de um comando select."
        return BdAccess.cur.fetchall()
 
    def persist(self):
        "realiza o commit das operações realizadas."
        if BdAccess.connected:
            BdAccess.conn.commit()
            return True
        else:
            return False

class VeiculoDAO:
    def __init__(self):
        "Quando a aplicação for executada pela primeira vez, cria-se o banco de dados"
        self.bd = BdAccess()
        self.bd.connect()
        self.bd.persist()

    def view(self):
        "recupera todos os dados do banco."
        rows = None
        try:
            self.bd.execute("SELECT * FROM veiculos")    
            rows = self.bd.fetchall()
        except sql.Error as error:
            print("Falha ao tentar selecionar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
            raise sql.Error()
        return rows

    def insert(self, veiculo):
        "insere novos registros no banco"
        try:
            self.bd.execute("INSERT INTO veiculos VALUES(NULL,?, ?,?,?,?,?,?,?,?,?,?,?,?,?)", (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.cor,veiculo.tanque, veiculo.combustivel, veiculo.consumo_cidade, veiculo.consumo_estrada, veiculo.tempo_0_100, veiculo.chassi, veiculo.placa, veiculo.tamanho_pneu,veiculo.som, veiculo.valor_diaria))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar inserir os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def search(self, veiculo):
        '''
        A função de busca utiliza o operador OR e todos os campos 
        que não forem preenchidos pelo usuário na hora da busca serão 
        considerados como strings vazias
        '''
        rows = None
        try:
            self.bd.execute("SELECT * FROM veiculos WHERE marca=? or modelo=? or ano=? or cor=? or tanque =? or combustivel =? or consumo_cidade =? or consumo_estrada =? or tempo_0_100 =? or chassi =? or placa =? or tamanho_pneu =? or som =? or valor_diaria =?", (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.cor,veiculo.tanque, veiculo.combustivel, veiculo.consumo_cidade, veiculo.consumo_estrada, veiculo.tempo_0_100, veiculo.chassi, veiculo.placa, veiculo.tamanho_pneu,veiculo.som, veiculo.valor_diaria))
            rows = self.bd.fetchall()
        except sqlite3.Error as error:
            print("Falha ao tentar buscar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
            raise Exception
        return rows

    def update(self, id, veiculo):
        "atualiza registros no banco"
        try:
            self.bd.execute("UPDATE veiculos SET marca =?, modelo=?, ano=?, cor=?, tanque =?, combustivel =?, consumo_cidade =?, consumo_estrada =?, tempo_0_100 =?, chassi =?, placa =?, tamanho_pneu =?, som =?, valor_diaria =? WHERE id = ?",(veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.cor,veiculo.tanque, veiculo.combustivel, veiculo.consumo_cidade, veiculo.consumo_estrada, veiculo.tempo_0_100, veiculo.chassi, veiculo.placa, veiculo.tamanho_pneu,veiculo.som, veiculo.valor_diaria, id))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar atualizar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
    
    def delete(self, id):
        "remove registros no banco"
        try:
            self.bd.execute("DELETE FROM veiculos WHERE id = ?", (id,))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar remover o registro")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def close(self):
        "fechar o banco"
        print('Fechando o Banco...')
        self.bd.disconnect()
