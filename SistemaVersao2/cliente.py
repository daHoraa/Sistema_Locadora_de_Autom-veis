from pessoa import Pessoa

class Cliente(Pessoa):
       def __init__(self,  numero_cnh ="", numero_registro_cnh ="", data_validade_cnh ="", 
                     uf_cnh ="", contato_emergencial ="", nome_contato_emergencial =""):
              #dados da cnh
              self.numero_cnh = numero_cnh
              self.numero_registro_cnh = numero_registro_cnh
              self.data_validade_cnh = data_validade_cnh
              self.uf_cnh = uf_cnh
              
              # contato emergencial / opcional 
              self.contato_emergencial = contato_emergencial
              self.nome_contato_emergencial = nome_contato_emergencial
