from tkinter import *
from locacaoDAO import LocacaoDAO
from veiculoDAO import Veiculo
import tkinter.messagebox
from datetime import datetime



class EfetuaLocacao(Toplevel):
    '''Classe interface locar veiculo'''
    def __init__(self, master=None):
        
        Toplevel.__init__(self, master=master)
        self.veiculo = Veiculo()
        self.dao = LocacaoDAO()

        self.geometry('1500x850+0+0')
        self.title('Locar veículo')
        self.resizable(0, 0)  # impede de maximizar
        self.configure(background='#c9c9ff')

        self.valores_diarias = []
        self.lista_compra_final = []
        
        # VARIAVEIS DE DATA
        now = datetime.now() # current date and time
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")


        # GUI ==============================================
        self.id_veiculo = Label(self , text="Código do veículo :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.id_veiculo.place(x=700, y=70)
        self.id_veiculo_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.id_veiculo_entry.place(x=1000, y=70)

        self.valor_locacao = Label(self , text="Valor total:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.valor_locacao.place(x=700, y=120)

        
        '''
        self.valor_locacao_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.valor_locacao_entry.place(x=1000, y=120)
        '''
        # BOTOES SUPERIORESS ===================================================================
        self.botao_calcular_pagamento = Button(self, text="Calcular \npagamento", width=10, height=4, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'), command=self.calcular)
        self.botao_calcular_pagamento.place(x=700, y=180)

        self.botao_locar_veiculo = Button(self, text="Finalizar \nlocacao", width=10, height=4, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'))
        self.botao_locar_veiculo.place(x=920, y=180)

        self.botao_sair = Button(self, text="Sair", width=10, height=4, bg='#ffb3ba', fg='black', font=(
            'Verdana 15 bold'), command=self.close)
        self.botao_sair.place(x=1135, y=180)
        
        self.data_inicial = Label(self , text="Data inicial :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.data_inicial.place(x=80, y=70)
        self.data_inicial_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.data_inicial_entry.place(x=370, y=70)
        self.data_inicial_entry.insert(END, date_time)

        self.id_cliente = Label(self , text="Código do cliente :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.id_cliente.place(x=80, y=120)
        self.id_cliente_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.id_cliente_entry.place(x=370, y=120)

        self.data_final = Label(self , text="Data final :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.data_final.place(x=80, y=170)
        self.data_final_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.data_final_entry.place(x=370, y=170)

        self.quant_diarias = Label(self , text="Quantidade de diárias :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.quant_diarias.place(x=80, y=220)
        self.quant_diarias_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.quant_diarias_entry.place(x=370, y=220)

        self.valor_diaria = Label(self , text="Valor da diária :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.valor_diaria.place(x=80, y=270)
        self.valor_diaria_entry = Entry(self , width=20, font=(
        'Verdana 15 bold'))
        self.valor_diaria_entry.place(x=370, y=270)

        # BOX PARA ESCOLHER O VEICULO =====================================================================
        self.veiculostxt = Label(self , text="Escolha um veículo:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.veiculostxt.place(x=30, y=340)
        self.lista_veiculos = Listbox(self , width=90, height=7, font=(
            'Verdana 15 bold'))
        self.lista_veiculos.place(x=30, y=370)
        self.scrollbar_veiculos = Scrollbar(self )
        self.lista_veiculos.configure(yscrollcommand=self.scrollbar_veiculos.set)
        self.scrollbar_veiculos.configure(command=self.lista_veiculos.yview)
        self.scrollbar_veiculos.place(x=1293, y=370, relheight=0.22)
        self.botao_selecionar_veiculo = Button(self, text="Selecionar \n veiculo", width=10, height=5, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'))
        self.botao_selecionar_veiculo.place(x=1320, y=400)
       
        # BOX PARA ESCOLHER O CLIENTE
        self.clientestxt = Label(self , text="Escolha um cliente:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.clientestxt.place(x=30, y=570)
        self.lista_clientes = Listbox(self , width=90, height=7, font=(
            'Verdana 15 bold'))
        self.lista_clientes.place(x=30, y=600)
        self.scrollbar_clientes = Scrollbar(self )
        self.lista_clientes.configure(yscrollcommand=self.scrollbar_clientes.set)
        self.scrollbar_clientes.configure(command=self.lista_clientes.yview)
        self.scrollbar_clientes.place(x=1293, y=600, relheight=0.22)
        self.botao_selecionar_cliente = Button(self, text="Selecionar \n cliente", width=10, height=5, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'))
        self.botao_selecionar_cliente.place(x=1320, y=625)
        

    def update_list(self):
        try:
            self.lista_locacoes.delete(0, END)
            for item in self.dao.view():
                self.lista_locacoes.insert(END, item)
        except Exception:
            print('Erro na lista clientes.')
    
    def calcular(self):
        # VARIAVEIS PARA CALCULAR QUANTIDADE DE DIARIAS
                
        valor_total = StringVar()
        var_quant_diarias = int(self.quant_diarias_entry.get())
        var_valor_diaria = int(self.valor_diaria_entry.get())
        total = var_quant_diarias*var_valor_diaria
        
        valor_total.set(total)
        self.valor_locacao_variavel = Label(self , textvariable=valor_total, bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.valor_locacao_variavel.place(x=1000, y=120)

        '''
        
        #var_data_final = self.data_final_entry.get()
        
        '''

    def get_items(self):
        self.locacao.id_cliente = self.id_cliente_entry.get()
        self.locacao.id_veiculo = self.id_veiculo_entry.get()
        self.locacao.data_inicial = self.data_inicial_entry.get()
        self.locacao.data_final = self.data_final_entry.get()
        self.locacao.quant_diarias = self.quant_diarias_entry.get()
        self.locacao.valor_locacao = self.valor_locacao_entry.get()

        if(self.cliente.nome == '' or self.cliente.rg == '' or self.cliente.cpf == '' or self.cliente.email == '' or self.cliente.telefone == '' or self.cliente.nascimento == '' or self.cliente.estado_civil == '' or self.cliente.genero == '' or self.cliente.cep == '' or self.cliente.logradouro == '' or self.cliente.bairro == '' or self.cliente.numero_logradouro == '' or self.cliente.cidade == '' or self.cliente.estado == '' or self.cliente.complemento == '' or self.cliente.numero_cnh == '' or self.cliente.numero_registro_cnh == '' or self.cliente.data_validade_cnh == '' or self.cliente.uf_cnh == '' or self.cliente.contato_emergencial == '' or self.cliente.nome_contato_emergencial == ''):
            tkinter.messagebox.showinfo(
                "Aviso:", "Preencha todos os campos!")
        else:
            try:
                self.cliente.telefone = int(self.cliente.telefone)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'O campo telefone deve ser preenchido com número!')
            
    def close(self):
        self.dao.close()
        self.destroy()

    def run(self):
        self.mainloop()

#EfetuaLocacao().run()