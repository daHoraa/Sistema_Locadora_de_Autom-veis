import sqlite3


class DataBaseAccess():
    '''Classe para a conexão com o banco de dados.'''
    database = 'locadora.db'
    conn = None
    cur = None
    connected = False

    def connect(self):
        '''Realiza a conexão com o banco de dados.'''
        try:
            DataBaseAccess.conn = sqlite3.connect(DataBaseAccess.database)
            DataBaseAccess.cur = DataBaseAccess.conn.cursor()
            DataBaseAccess.connected = True
        except sqlite3.Error as error:
            print('Erro no banco de dados: ', error)

    def disconnect(self):
        '''Fecha a conexão atual com o banco de dados.'''
        DataBaseAccess.conn.close()
        DataBaseAccess.connected = False

    def execute(self, sql, parametros=None):
        '''
        Executa um comando no banco de dados. recebe três parâmetros:
        * self: referencia para o próprio objeto. não precisa ser informado;
        * sql: comando SQL a ser executado;
        * parametro: lista com os parâmetros do comando SQL. Pode ser omitido.
        '''
        if DataBaseAccess.connected:
            if parametros == None:
                DataBaseAccess.cur.execute(sql)
            else:
                DataBaseAccess.cur.execute(sql,parametros)
            return True
        else:
            return False
    
    def fetchall(self):
        '''Recupera a tupla obtida com o comando SELECT.'''
        return DataBaseAccess.cur.fetchall()
    
    def persist(self):
        '''Realiza o commit das operações realizadas no Banco de Dados.'''
        if DataBaseAccess.connected:
            DataBaseAccess.conn.commit()
            return True
        else:
            return False

