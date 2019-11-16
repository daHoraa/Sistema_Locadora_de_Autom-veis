## Locadora 4x4

Um software para de aluguel de veículos para a disciplina de Programação Orientada a Objetos lecionada pelo professor Filipe Dwan na UFRR, campus Paricarana, 2019.2.
 
# Instalação

## Precompilado

É provido uma versão pré-compilada da aplicação para usuários dos
sistemas operacionais Windows e Linux, testados nos sistemas Windows
7, Windows 10 e a distribuição ArchLinux.  A pré-compilação é feita
através do software pyinstaller que embarca todas as dependências,
bibliotecas dinâmicas e a máquina virtual de Python num único
executável para simplificar todo o processo de distribuir o software.

Para baixar acesse: [release]

## Compilar manualmente

Para compilar manualmente você irá precisar de uma versão compatível
do Python, onde no caso foi testada apenas a versão 3.6.1 de Python,
logo é recomendado novamente usar a versão pré-compilada.

Caso você insistir em compilar manualmente, os passos assumem que você
tem a instalação do gerenciador de pacotes de Python **pip**
disponível no PATH do seu sistema, além do disponível git, então instalar:

``` bash
git clone https://www.github.com/ryukinix/rentalcar/
cd rentalcar
pip install -r requirements.txt
```

Caso você esteja no Windows, talvez você tenha problemas em relação a instalar
o PyQt5 por causa do `pywin32`, esse problema é descrito e resolvido em
[NOTAS.org](./NOTAS.org) (eu falei pra você usar a versão compilada de toda maneira).

Após isso, você pode executar a aplicação clicando em **run.py** ou executando pelo
terminal.

 ## Interface Gráfica     
 Segundo o site [devmedia](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956) existem diversos frameworks e ferramentas que permitem a criação interfaces gráficas em python, são alguns deles: WxWidgets; Tkinter; Kivy; PyGTK; PySide; QT.   
Porém, para este projetos usaremos apenas o Tkinter por possuir como vantagem a sua facilidade de uso e recursos disponíveis. Outra vantagem é que é nativo da linguagem Python, tudo o que precisamos fazer é importá-lo no momento do uso, ou seja, estará sempre disponível.


|Nome        |Versão   |
|------------|---------|
|Python      | 3.6.1   |
|PyQt5       | 5.9.2   |
|Qt          | 5.9.2   |
|Qt Designer | 5.9.2   |
|Emacs       | 27.0.1  |

