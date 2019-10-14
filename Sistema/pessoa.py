from endereco import *

class Pessoa(Endereco):
  def __init__(self, nome, rg, cpf, nascimento, estado_civil, sexo, CEP, rua, bairro, n_casa, cidade, estado):
    self.nome = nome
    self.rg = rg
    self.nascimento = nascimento
    self.estado_civil = estado_civil
    self.sexo = sexo
    super().__init__(CEP, rua, bairro, n_casa, cidade, estado)
  
 
    
