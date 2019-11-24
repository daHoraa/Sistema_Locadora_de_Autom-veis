from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, END, Toplevel, Frame, X
from cadastrar_veiculo import CadastroVeiculo
from cadastrar_cliente import CadastroCliente
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

        self.frame2.pack(side='bottom', anchor='ne')
        #self.frame2.place(side = 'RIGHT')

        self.frame1.pack()
        self.frame1.place(relx=.4, rely=.5, anchor="w")

        self.frame3.pack()
        self.frame3.place(relx=.5, rely=.5, anchor="c")

        self.heading = Label(self.frame1, text="4x4 Sistema de locação", bg='#c9c9ff', fg='black', font=(
            'Verdana 16 bold'))
        self.heading.pack(fill=X, pady=0)

        # BOTOES CLIENTE  =========================================================================
        self.BotaoCadastrarCliente = Button(self.frame1, text="Cadastrar cliente", width=60, height=2, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'), command=self.cadastrar_cliente)
        self.BotaoCadastrarCliente.pack(fill=X, pady=0)

        self.BotaoAlterarCliente = Button(self.frame1, text="Alterar cliente", width=30, height=2, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'))
        self.BotaoAlterarCliente.pack(fill=X, pady=0)

        self.BotaoExcluirCliente = Button(self.frame1, text="Excluir cliente", width=60, height=2, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'))
        self.BotaoExcluirCliente.pack(fill=X, pady=0)

        # BOTOES VEICULO  =========================================================================
        self.BotaoCadastrarVeiculo = Button(self.frame1, text="Cadastrar veiculo", width=30, height=2, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'), command=self.cadastrar_veiculo)
        self.BotaoCadastrarVeiculo.pack(fill=X, pady=0)

        self.BotaoAlterarVeiculo = Button(self.frame1, text="Alterar veiculo", width=30, height=2, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'))
        self.BotaoAlterarVeiculo.pack(fill=X, pady=0)

        self.BotaoExcluirVeiculo = Button(self.frame1, text="Excluir veiculo", width=30, height=2, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'))
        self.BotaoExcluirVeiculo.pack(fill=X, pady=0)

        # BOTOES LOCACAO E SAIR  =========================================================================
        self.BotaoEfetuarLocacao = Button(self.frame1, text="Efetuar locação", width=30, height=2, bg='#c8a2c8', fg='black', font=(
            'Verdana 15 bold'))
        self.BotaoEfetuarLocacao.pack(fill=X, pady=0)

        self.BotaoSair = Button(self.frame1, text="Sair", width=22, height=2, bg='#ffb3ba', fg='black', font=(
            'Verdana 15 bold'), command=self.close)
        self.BotaoSair.pack(fill=X, pady=0)

        '''
              self.Botao1 = Button(self.frame1, text='Clique nesse botão para alterar.', command=self.alterar, bg='darkred')

              self.entrada1 = Label(self.frame2, text='Usuário:', width=8, height=2, bg='#baffc9', fg='black', font=('Verdana 15 bold'))
              self.entrada1.place(x=0, y=1000)

              self.entrada2 = Entry(self.frame2)


              self.Botao1.pack()
              self.entrada1.pack(side=LEFT)
              self.entrada2.pack(side=LEFT)
              '''
    '''
    def alterar(self):

        self.BotaoCadastrarCliente.pack_forget()  # Retiro todos esses
        self.BotaoAlterarCliente.pack_forget()  # Retiro todos esses
        self.BotaoExcluirCliente.pack_forget()  # Retiro todos esses
        self.BotaoCadastrarVeiculo.pack_forget()  # Retiro todos esses
        self.BotaoAlterarVeiculo.pack_forget()  # Retiro todos esses
        self.BotaoExcluirVeiculo.pack_forget()  # Retiro todos esses
        self.BotaoEfetuarLocacao.pack_forget()  # Retiro todos esses

    '''
        # self.BotaoSair.pack_forget() #Retiro todos esses
        # self.heading.pack_forget() #Retiro todos esses
    '''
              self.Botao1.pack_forget() #Retiro todos esses

              self.entrada1.pack_forget() #Retiro todos esses
              self.entrada2.pack_forget() #Retiro todos esses

              # E no frame aonde os três acima estavam, eu coloquei esses:
              self.Botao2 = Button(self.frame3, text='Clique nesse botão para voltar.', command=self.reverter, bg='darkgray')
              self.entrada3 = Label(self.frame2, text='Digite algo acima', height=2)
              self.entrada4 = Entry(self.frame1)

              self.Botao2.pack()
              self.entrada3.pack(side=LEFT)
              self.entrada4.pack(side=LEFT)
    '''
    '''
    #def reverter(self):
        self.Botao1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada2.pack() # Para reverter eu simplesmente dei .pack() nesses

        self.Botao2.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada2.pack() # Para reverter eu simplesmente dei .pack() nesses

        self.Botao3.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada2.pack() # Para reverter eu simplesmente dei .pack() nesses


        self.Botao2.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
        self.entrada3.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
        self.entrada4.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
        '''

    def cadastrar_veiculo(self):

        #self.alterar()
        CadastroVeiculo().run()
        '''
              def deletar_veiculo(self):
              DeleteVeiculo().run()
              '''

    def cadastrar_cliente(self):

        #self.alterar()
        CadastroCliente().run()

    def efetuar_locacao(self):
        Locacao().run()

    def close(self):
        # self.mainrun.quit
        self.master.destroy()

    def mainrun(self):
        self.master.mainloop()


if __name__ == '__main__':
       Main().mainrun()
