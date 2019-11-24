# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk
from tkinter import *
from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button

LARGE_FONT= ("Verdana", 13)


class SeaofBTCapp(tk.Tk):

    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        

        Label(text="4x4 Rent a Car S/A").pack()

        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # quais paginas poderao ser acessadas 
        for F in (StartPage, LoginAdministrador, LoginFuncionario):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Seja bem-vindo!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Sou o administrador",
                            command=lambda: controller.show_frame(LoginAdministrador))
        button.pack()


        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        Label(text="© 4x4 - Todos os direitos reservados").pack()

        button2 = tk.Button(self, text="Sou um funcionário",
                            command=lambda: controller.show_frame(LoginFuncionario))
        button2.pack()


class LoginAdministrador(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bem-vindo, administrador!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Voltar à página de entrada",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button3 = tk.Button(self, text="Cadastrar funcionário",
                            command=lambda: controller.show_frame(LoginFuncionario))
        button3.pack()

        button2 = tk.Button(self, text="Login",
                            command=lambda: controller.show_frame(LoginFuncionario))
        button2.pack()

        


class LoginFuncionario(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bem-vindo, funcionário!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Voltar à página de entrada",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Login",
                            command=lambda: controller.show_frame(LoginFuncionario))
        button2.pack()
     
app = SeaofBTCapp()
app.mainloop()