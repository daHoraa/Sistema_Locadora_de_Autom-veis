from pessoa import *
from veiculo import *

class Funcionario(Pessoa):
  def __init__(self, nome, rg, cpf, nascimento, estado_civil, sexo, CEP, rua, bairro, n_casa, cidade, estado, senha):
    super().__init__(nome, rg, cpf, nascimento, estado_civil, sexo, CEP, rua, bairro, n_casa, cidade, estado)
    self.senha = senha
