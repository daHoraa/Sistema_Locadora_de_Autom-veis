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

import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")
janela = Tk()
'''
instanciamos a classe TK() através da variável janela, que foi criada no final do código.
Essa classe permite que os widgets possam ser utilizados na aplicação.
'''
LoginFrame(janela)
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
