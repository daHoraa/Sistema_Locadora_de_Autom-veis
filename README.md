## Locadora 4x4

Modelaremos uma aplicação que permite que funcionários da locadora com certo grau de prioridade gerenciem os veiculos disponíveis para locação. 

Existirâo dois tipos de veículos: carros e motos;   
O funcionário poderá:
- Fornecer detalhes relevantes sobre veículos disponíveis   
- listar todos os veículos disponíveis   
- marcar um veículo como alugado ou indisponível (por estar em manuteção, etc)
Para que nosso sistema tenha um grau elevado de detalhamento, haverá meio de informar se um carro alugado foi batido ou roubado.

## Classes:
  - Funcionario
  - Veiculo (Superclasse de carro e moto)
  - Carro (é um tipo de veículo, portanto subclasse de veículo)
  - Moto (é um tipo de veículo, portanto subclasse de veículo)
  - Aluguel
  - Cliente
