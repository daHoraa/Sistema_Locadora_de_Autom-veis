from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, Scrollbar, END, Frame, Pack, LEFT, RIGHT, YES, BOTH, VERTICAL
from locacaoDAO import LocacaoDAO
from veiculo import Veiculo
import tkinter.messagebox
import datetime


class Locacao:
    def __init__(self, master=''):

        self.master = master

        self.veiculo = Veiculo()
        self.dao = LocacaoDAO()

        self.preco_produtos = []
        self.lista_compra_final = []

        self.window = Tk()
        self.window.geometry('1350x850+0+0')
        self.window.title('Locar veículo')
        self.window.resizable(0, 0)  # impede de maximizar

        # code ========================================================================= 
        self.cod_veiculo = Label(self.master, text="Código do veículo :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.cod_veiculo.place(x=10, y=70)
        self.cod_veiculo_entry = Entry(self.master, width=35, font=(
        'Verdana 15 bold'))
        self.cod_veiculo_entry.place(x=300, y=70)

        self.cod_cliente = Label(self.master, text="Código do cliente :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.cod_cliente.place(x=10, y=120)
        self.cod_cliente_entry = Entry(self.master, width=35, font=(
        'Verdana 15 bold'))
        self.cod_cliente_entry.place(x=300, y=120)

        self.data_inicio = Label(self.master, text="Data do início :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.data_inicio.place(x=10, y=170)
        self.data_inicio_entry = Entry(self.master, width=35, font=(
        'Verdana 15 bold'))
        self.data_inicio_entry.place(x=300, y=170)

        
        self.quant_diarias = Label(self.master, text="Quantidade de diárias :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.quant_diarias.place(x=10, y=220)
        self.quant_diarias_entry = Entry(self.master, width=35, font=(
        'Verdana 15 bold'))
        self.quant_diarias_entry.place(x=300, y=220)

    def run(self):
        self.window.mainloop()

#Locacao().run()