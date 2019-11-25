from dao import DataBaseAccess, sqlite3
from cliente import Cliente

class ClienteDAO:
    def __init__(self):
        '''Irá se conectar ao banco de dados'''
        self.database = DataBaseAccess()
        self.database.connect()
        self.database.persist()


    def view(self):
        resultado = None
        try:
            self.database.execute("SELECT * FROM clientes")
            resultado = self.database.fetchall()
        except sqlite3.Error:
            print("Falha ao selecionar o registro.")
        return resultado


    def insert(self, cliente):
        '''Insere os funcionarios no banco de dados'''
        try:
            self.database.execute("INSERT INTO clientes(nome, rg, cpf, email, telefone, nascimento, estado_civil, genero, cep, logradouro, bairro, numero_logradouro, cidade, estado, complemento, numero_cnh, numero_registro_cnh, data_validade_cnh,uf_cnh, contato_emergencial, nome_contato_emergencial) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
            (cliente.nome, cliente.rg, cliente.cpf, cliente.email,  cliente.telefone,  cliente.nascimento,  cliente.estado_civil,  cliente.genero,  cliente.cep,  cliente.logradouro,  cliente.bairro,  cliente.numero_logradouro,  cliente.cidade,  cliente.estado,  cliente.complemento,  cliente.numero_cnh,  cliente.numero_registro_cnh,  cliente.data_validade_cnh,  cliente.uf_cnh,  cliente.contato_emergencial,  cliente.nome_contato_emergencial  ))
            self.database.persist()
        except sqlite3.Error:
            print("Falha ao tentar inserir no banco de dados.")


    def update(self, cliente, nome):
        '''Irá atualizar os registros no banco de dados'''
        try:
            self.database.execute("UPDATE clientes SET nome =?, rg =?, cpf =?, email =?, telefone =?, nascimento =?, estado_civil =?, genero =?, cep =?, logradouro =?, bairro =?, numero_logradouro =?, cidade =?, estado =?, complemento =?, numero_cnh =?, numero_registro_cnh =?, data_validade_cnh =?,uf_cnh =?, contato_emergencial =?, nome_contato_emergencial WHERE nome=?", (cliente.nome, cliente.rg, cliente.cpf, cliente.email,  cliente.telefone,  cliente.nascimento,  cliente.estado_civil,  cliente.genero,  cliente.cep,  cliente.logradouro,  cliente.bairro,  cliente.numero_logradouro,  cliente.cidade,  cliente.estado,  cliente.complemento,  cliente.numero_cnh,  cliente.numero_registro_cnh,  cliente.data_validade_cnh,  cliente.uf_cnh,  cliente.cep,  cliente.contato_emergencial,  cliente.nome_contato_emergencial))
            self.database.persist()
        except sqlite3.Error:
            print("Falha ao tentar inserir.")


    def delete(self, nome):
        "Deleta os registros do bando de dados"
        try:
            self.database.execute("DELETE FROM cliente WHERE nome=?", ())
            self.database.persist()
        except sqlite3.Error as error:
            print("Falha ao tentar remover o registro")
            print("Classe de exceção: ", error.__class__)
            print("Exceção é ", error.args)

    def close(self):
        '''Fechar conexão com o banco de dados'''
        self.database.disconnect()
        

    
    
