from pessoa import Pessoa

class Cliente(Pessoa):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

'''
class Pessoa(Endereco):
  def __init__(self, nome, rg, cpf, nascimento, estado_civil, sexo, CEP, rua, bairro, n_casa, cidade, estado):
    super().__init__(CEP, rua, bairro, n_casa, cidade, estado)
    self._nome = nome
    self._rg = rg
    self._nascimento = nascimento
    self._estado_civil = estado_civil
    self._sexo = sexo
  
  def _set_nome(self,nome):
      if not isinstance(nome, str):
        raise TypeError("Nome: entre com uma string")
      if len(nome < 3):
        raise TypeError("Nome: entre com seu nome completo")
        self._nome = nome

  def _get_nome(self):
        self._nome = nome
  
  def _set_cpf(self, cpf):
        assert valido.isValid()
        assert invalido.isValid()
'''