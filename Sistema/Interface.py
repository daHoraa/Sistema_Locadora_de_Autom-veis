try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk

'''importamos todos os componentes do módulo Tkinter'''

class Interface:
    '''
    Criamos uma classe chamada Application.
    É nela que criaremos os controles que serão exibidos na tela.
    '''
    def __init__(self, master=None):
        pass

root = Tk()
'''
instanciamos a classe TK() através da variável root, que foi criada no final do código.
Essa classe permite que os widgets possam ser utilizados na aplicação.
'''
Application(root)
'''
passamos a variável root como parâmetro do método
construtor da classe Application. 
'''
root.mainloop()
'''
chamamos o método root.mainloop() para exibirmos a tela.
Sem o event loop, a interface não será exibida.
'''
