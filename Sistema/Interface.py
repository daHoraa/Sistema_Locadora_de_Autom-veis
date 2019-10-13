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

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuario" and senha == "123":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

janela = Tk()
'''
instanciamos a classe TK() através da variável janela, que foi criada no final do código.
Essa classe permite que os widgets possam ser utilizados na aplicação.
'''
Interface(janela)
'''
passamos a variável janela como parâmetro do método
construtor da classe Application. 
'''
#altera o titulo da janela
janela.title("Locadora 4x4")

#altera a cor do fundo.
janela["bg"] = "pink"

#LARGURAxALTURA + ESQUERDA + DISTANCIA DO TOPO
#300X300+100+100
janela.geometry("1000x500+100+100")

janela.mainloop()
'''
chamamos o método janela.mainloop() para exibirmos a tela.
Sem o event loop, a interface não será exibida.
Interrompe o script enquanto a janela principal estiver aberta
'''
