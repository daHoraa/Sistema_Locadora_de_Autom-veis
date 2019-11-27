
class Pessoa():
  def __init__(self, nome='', rg='', cpf='', email='', telefone='', nascimento='', estado_civil='', 
                     genero='', cep='', logradouro='', bairro='', numero_logradouro='', cidade='', estado='', complemento=''):
       self.nome = nome
       self.rg = rg
       self.cpf = cpf

       self.email = email
       self.telefone = telefone # enviar codigo sms

       self.nascimento = nascimento
       self.estado_civil = estado_civil
       self.genero = genero

       #dados endereço
       self.cep = cep 
       self.logradouro = logradouro # rua, av, praça, alameda, rodovia, travessa, estrada, quadra, vila, avenida
       self.numero_logradouro = numero_logradouro
       self.complemento = complemento #opcional
       self.bairro = bairro
       self.cidade = cidade
       self.estado = estado