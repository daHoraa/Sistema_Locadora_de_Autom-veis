from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, END, Toplevel, Frame, X
from cadastrar_veiculo import CadastroVeiculo
from cadastrar_cliente import CadastroCliente
from alterar_cliente import AlteraCliente
from alterar_veiculo import AlteraVeiculo
from efetuar_locacao import EfetuaLocacao
from devolver_veiculo import DevolveVeiculo
#from produto_atualizar import ProdutoAtualiza
from delete_veiculo import DeleteVeiculo
#from fornecedor.fornecedor_atualizar import FornecedorAtualizar
# rom fornecedor.fornecedor_deletar import FornecedorDeletar
from locacao import Locacao
from clienteDAO import ClienteDAO
from cliente import Cliente
import tkinter.messagebox
import datetime


class Main(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)
        self.master.title('Locadora 4x4')
        self.master.geometry('1500x850+0+0')
        self.master.resizable(0, 0)  # impede de maximizar
        self.master['bg'] = '#c9c9ff'

        self.frame1 = Frame(self.master)
        self.frame2 = Frame(self.master)
        self.frame3 = Frame(self.master)

        self.frame2.pack(side='left')
        self.frame2.place(relx=.4, rely=.5, anchor="e")
        
        self.frame1.pack()
        self.frame1.place(relx=.4, rely=.5, anchor="w")

        self.frame3.pack()
        self.frame3.place(relx=.5, rely=.1, anchor="n")
        
        self.heading = Label(self.frame3, text="4x4 Sistema de locação", bg='#c9c9ff', fg='black', font=(
            'Verdana 16 bold'))
        self.heading.pack(pady=0)
        
        # BOTOES CLIENTE  =========================================================================
        self.BotaoCadastrarCliente = Button(self.frame1, text="Cadastrar cliente", width=48, height=2, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'), command=self.cadastrar_cliente)
        self.BotaoCadastrarCliente.pack(fill=X, pady=0)

        self.BotaoAlterarCliente = Button(self.frame1, text="Alterar cliente", width=30, height=2, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'), command = self.altera_cliente)
        self.BotaoAlterarCliente.pack(fill=X, pady=0)

        self.BotaoExcluirCliente = Button(self.frame1, text="Excluir cliente", width=48, height=2, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'))
        self.BotaoExcluirCliente.pack(fill=X, pady=0)

        # BOTOES VEICULO  =========================================================================
        self.BotaoCadastrarVeiculo = Button(self.frame1, text="Cadastrar veiculo", width=48, height=2, bg='#c8a2c8', fg='black', font=(
            'Verdana 15 bold'), command=self.cadastrar_veiculo)
        self.BotaoCadastrarVeiculo.pack(fill=X, pady=0)

        self.BotaoAlterarVeiculo = Button(self.frame1, text="Editar veiculo", width=48, height=2, bg='#c8a2c8', fg='black', font=(
            'Verdana 15 bold'), command = self.altera_veiculo)
        self.BotaoAlterarVeiculo.pack(fill=X, pady=0)

        self.BotaoExcluirVeiculo = Button(self.frame1, text="Excluir veiculo", width=30, height=2, bg='#c8a2c8', fg='black', font=(
            'Verdana 15 bold'))
        self.BotaoExcluirVeiculo.pack(fill=X, pady=0)

        # BOTOES LOCACAO E SAIR  =========================================================================
        self.BotaoEfetuarLocacao = Button(self.frame2, text="Efetuar locação", width=30, height=9, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'), command=self.efetuar_locacao)
        self.BotaoEfetuarLocacao.pack(fill=X, pady=0)

        self.BotaoDevolverVeiculo = Button(self.frame2, text="Devolver veiculo", width=30, height=9, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'), command=self.devolve_veiculo)
        self.BotaoDevolverVeiculo.pack(fill=X, pady=0)

        self.BotaoSair = Button(self.frame1, text="Sair", width=22, height=2, bg='#ffb3ba', fg='black', font=(
            'Verdana 15 bold'), command=self.close)
        self.BotaoSair.pack(fill=X, pady=0)
    
    def cadastrar_veiculo(self):
        CadastroVeiculo().run()

        '''
        def deletar_veiculo(self):
        DeleteVeiculo().run()
        '''

    def altera_veiculo(self):
        AlteraVeiculo().run()

    def cadastrar_cliente(self):
        CadastroCliente().run()

    def altera_cliente(self):    
        AlteraCliente().run()

    def efetuar_locacao(self):
        EfetuaLocacao().run()

    def devolve_veiculo(self):
        DevolveVeiculo().run()

    def close(self):
        self.master.destroy()

    def mainrun(self):
        self.master.mainloop()


if __name__ == '__main__':
       Main().mainrun()
