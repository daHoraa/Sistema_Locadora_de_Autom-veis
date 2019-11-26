from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, END, Toplevel
from veiculoDAO import VeiculoDAO
from veiculo import Veiculo
import tkinter.messagebox


class DeleteVeiculo(Toplevel):
    '''Classe interface deletar veiculo'''

    def __init__(self, master=None):
        '''Inicializa uma nova tela para deletar os veiculos.'''
        Toplevel.__init__(self, master=master)
        self.veiculo = Veiculo()
        self.dao = VeiculoDAO()
        self.geometry('1350x850+0+0')
        self.title('Deletar Veiculos')
        self.resizable(0, 0)
        self.configure(background='#c9c9ff')
        
        self.id = None
        self.nome_tela = Label(self, text="Deletar Veiculos", bg='#c9c9ff', fg='white', font=(
            'Verdana 40 bold'))
        self.nome_tela.place(x=500, y=50)

        # BOTOES =================================================================
        self.botao_deletar = Button(self, text="Deletar veiculo do banco de dados", width=43, height=1, bg='#baffc9', fg='black', font=(
            'Verdana  15 bold'), command=self.delete)
        self.botao_deletar.place(x=40, y=600)

        self.botao_sair = Button(self, text="Sair", width= 43, height=1, bg='#ffb3ba', fg='black', font=(
            'Verdana  15 bold'), command=self.close)
        self.botao_sair.place(x=690, y=600)

        self.listbox_veiculos = Listbox(self, width=90, height=10, font=(
            'Verdana  15 bold'))
        self.listbox_veiculos.place(x=40, y=300)


        # SCROLLBAR =========================================================
        self.scrollbar_veiculo = Scrollbar(self, )
        self.listbox_veiculos.configure(yscrollcommand=self.scrollbar_veiculo.set)
        self.scrollbar_veiculo.configure(command=self.listbox_veiculos.yview)
        self.scrollbar_veiculo.place(
            x=1340, y=120, relheight=0.62, anchor='ne')

        # AREA PESQUISAR =======================================================
        self.pesquisar_veiculo = Label(self, text="Pesquisar pela marca:", bg='#c9c9ff', font=(
            'Verdana  15 bold'))
        self.pesquisar_veiculo.place(x=40, y=200)

        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index,
                              mode: self.update_list())
        self.search_entry = Entry(self, textvariable=self.search_var, width=20, font=(
            'Verdana  15 bold'))
        self.search_entry.place(x=300, y=200)
        
        self.botao_pesquisar = Button(self, text="Pesquisar", width= 20, height=1, bg='#ffdfba', fg='black', font=(
            'Verdana  15 bold'), command=self.close)
        self.botao_pesquisar.place(x=620, y=190)

        self.view_command()

        self.listbox_veiculos.bind('<<ListboxSelect>>', self.selecionar_list_box)

    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.listbox_veiculos.delete(0, END)
            for r in rows:
                self.listbox_veiculos.insert(END, r)
        except Exception as e:
            print(e)

    def selecionar_list_box(self, event):
        if self.listbox_veiculos.curselection():
            indice = self.listbox_veiculos.curselection()[0]
            self.selecionado = self.listbox_veiculos.get(indice)

            self.id = self.selecionado[0]

    def delete(self):
        '''Função para deletar o veiculo do banco de dados'''
        try:
            self.dao.delete(self.id)
        except Exception:
             tkinter.messagebox.showinfo(
                        'Aviso!', 'Erro ao acessar o banco de dados.')
        else:
            tkinter.messagebox.showinfo(
                'Aviso!', 'veiculo Excluido com Sucesso!')
            #self.clear_all()
            self.view_command()

    def close(self):
        '''Função para fechar a tela, fecha a conexão com o banco de dados e destroi a janela atual.'''
        self.dao.close()
        self.destroy()

    def run(self):
        '''Função para chamar a tela.'''
        self.mainloop()

#DeleteVeiculo().run()
