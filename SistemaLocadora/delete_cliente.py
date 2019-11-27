from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, END, Toplevel
from clienteDAO import ClienteDAO
from cliente import Cliente
import tkinter.messagebox
import datetime


class DeletaCliente(Toplevel):
    '''Classe interface cadastrar cliente'''

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        self.cliente = Cliente()
        self.dao = ClienteDAO()

        self.geometry('1500x850+0+0')
        self.title('Excluir cliente')
        self.resizable(0, 0)  # impede de maximizar
        self.configure(background='#c9c9ff')

        self.id = None

        self.heading = Label(self, text="Excluir um cliente do banco de dados", bg='#c9c9ff', fg='white', font=(
            'Verdana 20 bold'))
        self.heading.place(x=550, y=50)

        self.pesquisar_veiculo = Label(self, text="Pesquisar por nome:", bg='#c9c9ff', font=(
            'Verdana  15 bold'))
        self.pesquisar_veiculo.place(x=40, y=150)

        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index,
                              mode: self.view_command())
        self.search_entry = Entry(self, textvariable=self.search_var, width=20, font=(
            'Verdana  15 bold'))
        self.search_entry.place(x=300, y=150)

        # LIST BOX =============================================================
        self.lista_clientes = Listbox(self, width=95, height=10, font=(
            'Verdana 15 bold'))
        self.lista_clientes.place(x=40, y=300)

        # BOTOES =================================================================
        self.botao_deletar = Button(self, text="Deletar cliente do banco de dados", width=46, height=1, bg='#baffc9', fg='black', font=(
            'Verdana  15 bold'), command=self.delete)
        self.botao_deletar.place(x=40, y=600)

        self.botao_sair = Button(self, text="Sair", width=46, height=1, bg='#ffb3ba', fg='black', font=(
            'Verdana  15 bold'), command=self.close)
        self.botao_sair.place(x=720, y=600)

        # self.botao_pesquisar = Button(self, text="Pesquisar", width=20, height=1, bg='#ffdfba', fg='black', font=(
        #     'Verdana  15 bold'))
        # self.botao_pesquisar.place(x=620, y=140)

        # Associando a Scrollbar com a Listbox...
        self.scrollbar_cliente = Scrollbar(self)
        self.lista_clientes.configure(
            yscrollcommand=self.scrollbar_cliente.set)
        self.scrollbar_cliente.configure(command=self.lista_clientes.yview)
        self.scrollbar_cliente.place(
            x=1375, y=300, relheight=0.31, anchor='ne')

        self.pesquisar_cliente = Label(self, text="Lista de clientes cadastrados:", bg='#c9c9ff',  font=(
            'Verdana 15 bold'))
        self.pesquisar_cliente.place(x=40, y=260)

        self.view_command()
        self.lista_clientes.bind('<<ListboxSelect>>', self.selecionar_list_box)

    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.lista_clientes.delete(0, END)
            for r in rows:
                if str(self.search_var.get()).lower() in str(r).lower():
                    self.lista_clientes.insert(END, r)
        except Exception as e:
            print(e)

    # def get_items(self):
    #     self.cliente.nome = self.nome_entry.get()
    #     self.cliente.rg = self.rg_entry.get()
    #     self.cliente.cpf = self.cpf_entry.get()
    #     self.cliente.email = self.email_entry.get()
    #     self.cliente.telefone = self.telefone_entry.get()
    #     self.cliente.nascimento = self.nascimento_entry.get()
    #     self.cliente.estado_civil = self.estado_civil_entry.get()
    #     self.cliente.genero = self.genero_entry.get()

    def selecionar_list_box(self, event):
        if self.lista_clientes.curselection():
            indice = self.lista_clientes.curselection()[0]
            self.selecionado = self.lista_clientes.get(indice)

            self.id = self.selecionado[0]

    def delete(self):
        try:
            self.dao.delete(self.id)
        except Exception:
            tkinter.messagebox.showinfo(
                'Aviso!', 'Erro ao acessar o banco de dados.')
        else:
            tkinter.messagebox.showinfo(
                'Aviso!', 'Produto Excluido com Sucesso!')
            self.view_command()

    # def clear_all(self):
        # self.nome_entry.delete(0, END)
        # self.rg_entry.delete(0, END)
        # self.cpf_entry.delete(0, END)
        # self.email_entry.delete(0, END)
        # self.telefone_entry.delete(0, END)
        # self.nascimento_entry.delete(0, END)
        # self.estado_civil_entry.delete(0, END)
        # self.genero_entry.delete(0, END)
        # self.cep_entry.delete(0, END)
        # self.logradouro_entry.delete(0, END)
        # self.bairro_entry.delete(0, END)
        # self.numero_logradouro_entry.delete(0, END)
        # self.cidade_entry.delete(0, END)
        # self.estado_entry.delete(0, END)
        # self.complemento_entry.delete(0, END)
        # self.numero_cnh_entry.delete(0, END)
        # self.numero_registro_cnh_entry.delete(0, END)
        # self.data_validade_cnh_entry.delete(0, END)
        # self.uf_cnh_entry.delete(0, END)
        # self.contato_emergencial_entry.delete(0, END)
        # self.nome_contato_emergencial_entry.delete(0, END)
    '''
    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.lista_clientes.delete(0, END)
            for r in rows:
                self.lista_clientes.insert(END, r)
        except Exception as e:
            print(e)

    def search_command(self):
        "método para buscar registros"
        self.lista_clientes.delete(0, END)
        self.__fill_current_client()
        try:
            rows = self.dao.search(self.currentClient)
            for r in rows:
                self.gui.lista_clientes.insert(END, r)
        except Exception as e:
            print(e)
    '''

    def close(self):
        self.dao.close()
        self.destroy()

    def run(self):
        self.mainloop()


# DeletaCliente().run()
