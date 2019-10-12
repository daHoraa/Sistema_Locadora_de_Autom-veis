## Locadora 4x4

Modelaremos uma aplicação que permite que funcionários da locadora com certo grau de prioridade gerenciem os veiculos disponíveis para locação. 

Existirâo dois tipos de veículos: carros e motos;   
O funcionário poderá:
- Fornecer detalhes relevantes sobre veículos disponíveis   
- listar todos os veículos disponíveis   
- marcar um veículo como alugado ou indisponível (por estar em manuteção, etc)
Para que nosso sistema tenha um grau elevado de detalhamento, haverá meio de informar se um carro alugado foi batido ou roubado.

## Classes:   
  - [Pessoa](https://github.com/daHoraa/Sistema_Locadora_de_Autom-veis/blob/master/Sistema/Pessoa.py)
    - Funcionario   
    - Cliente
  - Veiculo (Superclasse de carro e moto)
    - Carro (é um tipo de veículo, portanto subclasse de veículo)
    - Moto (é um tipo de veículo, portanto subclasse de veículo)
  - Aluguel
 
 ## Interface Gráfica     
 Segundo o site [devmedia](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956) existem diversos frameworks e ferramentas que permitem a criação interfaces gráficas em python, são alguns deles: WxWidgets; Tkinter; Kivy; PyGTK; PySide; QT.   
Porém, para este projetos usaremos apenas o Tkinter por possuir como vantagem a sua facilidade de uso e recursos disponíveis. Outra vantagem é que é nativo da linguagem Python, tudo o que precisamos fazer é importá-lo no momento do uso, ou seja, estará sempre disponível.
