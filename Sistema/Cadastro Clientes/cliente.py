class Client:
    def __init__(self, nacionalidade ="", tipo_documento ="", genero ="", telefone ="", numero_cnh ="", numero_registro_cnh ="", data_validade_cnh ="", uf_cnh ="", rg ="", nascimento ="", cep ="", logradouro ="", endereco ="", numero_endereco ="", complemento ="", bairro ="", cidade ="", estado ="", contato_emergencial ="", nome_contato_emergencial ="", nome="", sobrenome="", email="", cpf=""):
        # dados pessoais
        self.nacionalidade = nacionalidade
        self.tipo_documento = tipo_documento
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.genero = genero 
        self.telefone = telefone # +55 (95) 98123 5170 enviar codio sms

        #dados da cnh
        self.numero_cnh = numero_cnh
        self.numero_registro_cnh = numero_registro_cnh
        self.data_validade_cnh = data_validade_cnh
        self.uf_cnh = uf_cnh 
        self.rg = rg
        self.nascimento = nascimento
        
        #dados endereço
        self.cep = cep 
        self.logradouro = logradouro # rua, av, praça, alameda, rodovia, travessa, estrada, quadra, vila, avenida
        self.endereco = endereco 
        self.numero_endereco = numero_endereco
        self.complemento = complemento #opcional
        self.bairro = bairro
        self.cidade = cidade 
        self.estado = estado

        # contato emergencial / opcional 
        self.contato_emergencial = contato_emergencial
        self.nome_contato_emergencial = nome_contato_emergencial

        #self.estado_civil = estado_civil

    def __str__(self):
        print(self.nacionalidade , self.tipo_documento , self.genero , self.telefone , self.numero_cnh , self.numero_registro_cnh , self.data_validade_cnh , self.uf_cnh , self.rg , self.nascimento, self.cep , self.logradouro , self.endereco , self.numero_endereco , self.complemento , self.bairro , self.cidade , self.estado, self.nome, self.sobrenome, self.email, self.cpf)
