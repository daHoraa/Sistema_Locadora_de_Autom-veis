import sqlite3 as sql
 
'''
* Para esta aplicação, precisamos apenas de uma tabela 
(que se chamará clientes), com os seguintes campos:
    * Id
    * Nome
    * Sobrenome
    * Email
    * CPF
'''

class BdAccess():
    database    = "clientes.db"
    conn        = None
    cur         = None
    connected   = False
 
    def connect(self):
        "realiza conexão com o banco de dados"
        try:
            BdAccess.conn = sql.connect(BdAccess.database)
            BdAccess.cur = BdAccess.conn.cursor()
            BdAccess.connected = True
            self.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY , nacionalidade TEXT, tipo_domumento TEXT, cpf TEXT, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT, genero TEXT, telefone TEXT, numero_cnh TEXT, numero_registro_cnh TEXT, data_validade_cnh TEXT, uf_cnh TEXT, rg TEXT, nascimento TEXT, cep TEXT, logradouro TEXT, endereco TEXT, numero_endereco TEXT, complemento TEXT, bairro TEXT, cidade TEXT, estado TEXT)")
        #except sqlite3.Error as error:
            #print("Erro no banco de dados: ", error)
    #fecha a conexão com o banco de dados
    

    #def disconnect(self):
        #BdAccess.conn.close()
        #BdAccess.connected = False

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
            self.bd.execute("INSERT INTO clientes VALUES(NULL, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ( self.nacionalidade , self.tipo_domumento , self.cpf , self.nome , self.sobrenome , self.email , self.cpf , self.genero , self.telefone , self.numero_cnh , self.numero_registro_cnh , self.data_validade_cnh , self.uf_cnh , self.rg , self.nascimento , self.cep , self.logradouro , self.endereco , self.numero_endereco , self.complemento , self.bairro , self.cidade , self.estado))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar inserir os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def search(self, cliente):
        '''
        A função de busca utiliza o operador OR e todos os campos 
        que não forem preenchidos pelo usuário na hora da busca serão 
        considerados como strings vazias
        '''
        rows = None
        try:
            self.bd.execute("SELECT * FROM clientes WHERE nacionalidade =? or tipo_documento =? or nome=? or sobrenome=? or email=? or cpf=? or cpf =? or genero =? or telefone =? or numero_cnh =? or numero_registro_cnh =? or data_validade_cnh =? or uf_cnh =? or rg =? or nascimento =? or cep = ? or logradouro = ? or endereco = ? or numero_endereco = ? or complemento = ? or bairro = ? or cidade = ? or estado = ?", (cliente.nacionalidade or cliente.tipo_domumento or cliente.nome or cliente.sobrenome or cliente.email or cliente.cpf or cliente.genero or cliente.telefone or cliente.numero_cnh or cliente.numero_registro_cnh or cliente.data_validade_cnh or cliente.uf_cnh or cliente.rg or cliente.nascimento or cliente.cep or cliente.logradouro or cliente.endereco or cliente.numero_endereco or cliente.complemento or cliente.bairro or cliente.cidade or cliente.estado))
            rows = self.bd.fetchall()
        except sqlite3.Error as error:
            print("Falha ao tentar buscar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
            raise Exception
        return rows

    def update(self, id, cliente):
        "atualiza registros no banco"
        try:
            self.bd.execute("UPDATE clientes SET nacionalidade =? ,tipo_domumento =? ,cpf =? ,nome =? ,sobrenome =? ,email =? ,cpf =? ,genero =? ,telefone =? ,numero_cnh =? ,numero_registro_cnh =? ,data_validade_cnh =? ,uf_cnh =? ,rg =? ,nascimento =? ,cep =? ,logradouro =? ,endereco =? ,numero_endereco =? ,complemento =? ,bairro =? ,cidade =? ,estado =? WHERE id = ?", (cliente.nacionalidade    , cliente.tipo_domumento    , cliente.cpf    , cliente.nome    , cliente.sobrenome    , cliente.email    , cliente.cpf    , cliente.genero    , cliente.telefone    , cliente.numero_cnh    , cliente.numero_registro_cnh    , cliente.data_validade_cnh    , cliente.uf_cnh    , cliente.rg    , cliente.nascimento    , cliente.cep    , cliente.logradouro    , cliente.endereco    , cliente.numero_endereco    , cliente.complemento    , cliente.bairro    , cliente.cidade    , cliente.estado , id))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar atualizar os registros")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)
    
    def delete(self, id):
        "remove registros no banco"
        try:
            self.bd.execute("DELETE FROM clientes WHERE id = ?", (id,))
            self.bd.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar remover o registro")
            print("Classe da exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def close(self):
        "fechar o banco"
        print('Fechando o Banco...')
        self.bd.disconnect()
