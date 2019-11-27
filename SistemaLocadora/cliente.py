from pessoa import Pessoa

class Cliente(Pessoa):
       def __init__(self,  numero_cnh ="", numero_registro_cnh ="", data_validade_cnh ="", 
                     uf_cnh ="", contato_emergencial ="", nome_contato_emergencial =""):
              Pessoa.__init__(self, nome ="",rg ="",cpf ="", email ="",telefone ="",nascimento ="",estado_civil ="",genero ="",cep ="",logradouro ="",numero_logradouro ="",complemento ="",bairro ="",cidade ="",estado="")
              #dados da cnh
              self.numero_cnh = numero_cnh
              self.numero_registro_cnh = numero_registro_cnh
              self.data_validade_cnh = data_validade_cnh
              self.uf_cnh = uf_cnh
              
              # contato emergencial / opcional 
              self.contato_emergencial = contato_emergencial
              self.nome_contato_emergencial = nome_contato_emergencial
