from tkinter import *
from locacaoDAO import LocacaoDAO
from veiculoDAO import Veiculo
from clienteDAO import ClienteDAO
from veiculoDAO import VeiculoDAO
from locacao import Locacao
import tkinter.messagebox
from datetime import datetime


class EfetuaLocacao(Toplevel):
    '''Classe interface locar veiculo'''

    def __init__(self, master=None):

        Toplevel.__init__(self, master=master)
        self.veiculo = Veiculo()
        self.dao = LocacaoDAO()
        self.dao_cliente = ClienteDAO()
        self.dao_veiculo = VeiculoDAO()

        self.geometry('1500x850+0+0')
        self.title('Locar veículo')
        self.resizable(0, 0)  # impede de maximizar
        self.configure(background='#c9c9ff')

        self.valores_diarias = []
        self.lista_compra_final = []

        self.locacao = Locacao()

        # VARIAVEIS DE DATA
        now = datetime.now()  # current date and time
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

        # GUI ==============================================
        self.id_veiculo = Label(self, text="Código do veículo :", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.id_veiculo.place(x=700, y=70)
        self.id_veiculo_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.id_veiculo_entry.place(x=1000, y=70)

        self.valor_locacao = Label(self, text="Valor total:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.valor_locacao.place(x=700, y=120)
        self.valor_locacao_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.valor_locacao_entry.place(x=1000, y=120)



        '''
        self.valor_locacao_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.valor_locacao_entry.place(x=1000, y=120)
        '''
        # BOTOES SUPERIORESS ===================================================================
        self.botao_calcular_pagamento = Button(self, text="Calcular \npagamento", width=10, height=4, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'), command=self.calcular_pagamento)
        self.botao_calcular_pagamento.place(x=700, y=180)

        self.botao_locar_veiculo = Button(self, text="Finalizar \nlocacao", width=10, height=4, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'), command = self.get_items)
        self.botao_locar_veiculo.place(x=920, y=180)

        self.botao_sair = Button(self, text="Sair", width=10, height=4, bg='#ffb3ba', fg='black', font=(
            'Verdana 15 bold'), command=self.close)
        self.botao_sair.place(x=1135, y=180)

        self.data_inicial = Label(self, text="Data inicial :", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.data_inicial.place(x=80, y=70)
        self.data_inicial_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.data_inicial_entry.place(x=370, y=70)
        self.data_inicial_entry.insert(END, date_time)

        self.id_cliente = Label(self, text="Código do cliente :", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.id_cliente.place(x=80, y=120)
        self.id_cliente_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.id_cliente_entry.place(x=370, y=120)

        # self.data_final = Label(self, text="Data final :", bg='#c9c9ff', fg='white', font=(
        #     'Verdana 15 bold'))
        # self.data_final.place(x=80, y=170)
        # self.data_final_entry = Entry(self, width=20, font=(
        #     'Verdana 15 bold'))
        # self.data_final_entry.place(x=370, y=170)

        self.quant_diarias = Label(self, text="Quantidade de diárias :", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.quant_diarias.place(x=80, y=220)
        self.quant_diarias_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.quant_diarias_entry.place(x=370, y=220)

        self.valor_diaria = Label(self, text="Valor da diária :", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.valor_diaria.place(x=80, y=270)
        self.valor_diaria_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.valor_diaria_entry.place(x=370, y=270)

        # BOX PARA ESCOLHER O VEICULO =====================================================================
        self.veiculostxt = Label(self, text="Escolha um veículo:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.veiculostxt.place(x=30, y=340)
        self.lista_veiculos = Listbox(self, width=90, height=7, font=(
            'Verdana 15 bold'))
        self.lista_veiculos.place(x=30, y=370)
        self.scrollbar_veiculos = Scrollbar(self)
        self.lista_veiculos.configure(
            yscrollcommand=self.scrollbar_veiculos.set)
        self.scrollbar_veiculos.configure(command=self.lista_veiculos.yview)
        self.scrollbar_veiculos.place(x=1293, y=370, relheight=0.22)
        # self.botao_selecionar_veiculo = Button(self, text="Selecionar \n veiculo", width=10, height=5, bg='#ffdfba', fg='black', font=(
        #     'Verdana 15 bold'))
        # self.botao_selecionar_veiculo.place(x=1320, y=400)

        # BOX PARA ESCOLHER O CLIENTE
        self.clientestxt = Label(self, text="Escolha um cliente:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.clientestxt.place(x=30, y=570)
        self.lista_clientes = Listbox(self, width=90, height=7, font=(
            'Verdana 15 bold'))
        self.lista_clientes.place(x=30, y=600)
        self.scrollbar_clientes = Scrollbar(self)
        self.lista_clientes.configure(
            yscrollcommand=self.scrollbar_clientes.set)
        self.scrollbar_clientes.configure(command=self.lista_clientes.yview)
        self.scrollbar_clientes.place(x=1293, y=600, relheight=0.22)
        # self.botao_selecionar_cliente = Button(self, text="Selecionar \n cliente", width=10, height=5, bg='#ffdfba', fg='black', font=(
        #     'Verdana 15 bold'))
        # self.botao_selecionar_cliente.place(x=1320, y=625)
        self.view_command()

        self.lista_veiculos.bind(
            '<<ListboxSelect>>', self.selecionar_list_box_veiculos)
        self.lista_clientes.bind(
            '<<ListboxSelect>>', self.selecionar_list_box_clientes)
    
    def calcular_pagamento(self):
        self.valor_locacao_entry.delete(0, END)
        self.valor_locacao_entry.insert(0, float(self.valor_diaria_entry.get()) * float(self.quant_diarias_entry.get()))

    def selecionar_list_box_veiculos(self, event):
        if self.lista_veiculos.curselection():
            indice = self.lista_veiculos.curselection()[0]
            self.selecionado = self.lista_veiculos.get(indice)
            self.id_veiculo_entry.delete(0, END)
            self.id_veiculo_entry.insert(0, self.selecionado[0])
            self.valor_diaria_entry.delete(0, END)
            self.valor_diaria_entry.insert(0, self.selecionado[14])


    def selecionar_list_box_clientes(self, event):
        if self.lista_clientes.curselection():
            indice = self.lista_clientes.curselection()[0]
            self.selecionado = self.lista_clientes.get(indice)
            self.id_cliente_entry.delete(0, END)
            self.id_cliente_entry.insert(0, self.selecionado[0])

    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao_cliente.view()
            self.lista_clientes.delete(0, END)
            for r in rows:
                self.lista_clientes.insert(END, r)
            rows = self.dao_veiculo.view()
            self.lista_veiculos.delete(0, END)
            for r in rows:
                self.lista_veiculos.insert(END, r)
        except Exception as e:
            print(e)

    # def calcular(self):
    #     # VARIAVEIS PARA CALCULAR QUANTIDADE DE DIARIAS

    #     valor_total = StringVar()
    #     var_quant_diarias = int(self.quant_diarias_entry.get())
    #     var_valor_diaria = int(self.valor_diaria_entry.get())
    #     total = var_quant_diarias*var_valor_diaria

    #     valor_total.set(total)
    #     self.valor_locacao_variavel = Label(self, textvariable=valor_total, bg='#c9c9ff', fg='white', font=(
    #         'Verdana 15 bold'))
    #     self.valor_locacao_variavel.place(x=1000, y=120)

        '''
        
        #var_data_final = self.data_final_entry.get()
        
        '''

    def get_items(self):
        self.locacao.id_cliente = self.id_cliente_entry.get()
        self.locacao.id_veiculo = self.id_veiculo_entry.get()
        self.locacao.data_inicial = self.data_inicial_entry.get()
        self.locacao.diarias = self.quant_diarias_entry.get()
        self.locacao.valor_locacao = self.valor_locacao_entry.get()

        if(self.locacao.id_cliente == '' or self.locacao.id_veiculo == '' or self.locacao.diarias == '' or self.locacao.valor_locacao == ''):
            tkinter.messagebox.showinfo(
                "Aviso:", "Preencha todos os campos!")
        else:
            try:
                self.dao.insert(self.locacao)
                tkinter.messagebox.showinfo(
                    'Aviso!', 'Dados Inseridos com sucesso!')
            except :
                tkinter.messagebox.showinfo(
                    'Aviso!', 'Erro ao inserir dados!')

    def close(self):
        self.dao.close()
        self.destroy()

    def run(self):
        self.mainloop()

# EfetuaLocacao().run()
