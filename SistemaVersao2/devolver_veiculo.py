from tkinter import *
from locacaoDAO import LocacaoDAO
from veiculoDAO import Veiculo
import tkinter.messagebox
import datetime


class DevolveVeiculo(Toplevel):
       '''Classe interface locar veiculo'''
       def __init__(self, master=None):
              Toplevel.__init__(self, master=master)
              self.veiculo = Veiculo()
              self.dao = LocacaoDAO()

              self.geometry('1500x850+0+0')
              self.title('Devolver veiculo locado')
              self.resizable(0, 0)  # impede de maximizar
              self.configure(background='#c9c9ff')

              self.valores_diarias = []
              self.lista_compra_final = []
              
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
              self.valor_locacao_entry = Entry(self , width=20, font=(
              'Verdana 15 bold'))
              self.valor_locacao_entry.place(x=1000, y=120)

              # BOTOES SUPERIORESS ===================================================================
              self.botao_calcular_pagamento = Button(self, text="Calcular \npagamento", width=10, height=4, bg='#baffc9', fg='black', font=(
              'Verdana 15 bold'))
              self.botao_calcular_pagamento.place(x=700, y=180)

              self.botao_locar_veiculo = Button(self, text="Confirmar \ndevolução", width=10, height=4, bg='#baffc9', fg='black', font=(
              'Verdana 15 bold'))
              self.botao_locar_veiculo.place(x=920, y=180)

              self.botao_sair = Button(self, text="Sair", width=10, height=4, bg='#ffb3ba', fg='black', font=(
              'Verdana 15 bold'), command = self.close)
              self.botao_sair.place(x=1135, y=180)
              
              self.data_inicial = Label(self , text="Data :", bg='#c9c9ff', fg='white', font=(
              'Verdana 15 bold'))
              self.data_inicial.place(x=80, y=70)
              self.data_inicial_entry = Entry(self , width=20, font=(
              'Verdana 15 bold'))
              self.data_inicial_entry.place(x=370, y=70)

              self.id_cliente = Label(self , text="Código do cliente :", bg='#c9c9ff', fg='white', font=(
              'Verdana 15 bold'))
              self.id_cliente.place(x=80, y=120)
              self.id_cliente_entry = Entry(self , width=20, font=(
              'Verdana 15 bold'))
              self.id_cliente_entry.place(x=370, y=120)

              self.data_final = Label(self , text="Data do início :", bg='#c9c9ff', fg='white', font=(
              'Verdana 15 bold'))
              self.data_final.place(x=80, y=170)
              self.data_final_entry = Entry(self , width=20, font=(
              'Verdana 15 bold'))
              self.data_final_entry.place(x=370, y=170)
              
              self.data_de_hoje = Label(self , text="Data de hoje :", bg='#c9c9ff', fg='white', font=(
              'Verdana 15 bold'))
              self.data_de_hoje.place(x=80, y=220)
              self.data_de_hoje_entry = Entry(self , width=20, font=(
              'Verdana 15 bold'))
              self.data_de_hoje_entry.place(x=370, y=220)
              self.data_final_entry.insert(END, datetime.date.today())


              # BOX PARA ESCOLHER O VEICULO
              self.locacoestxt = Label(self , text="Escolha um registro de locacao:", bg='#c9c9ff', fg='white', font=(
              'Verdana 15 bold'))
              self.locacoestxt.place(x=30, y=340)
              self.lista_locacoes = Listbox(self , width=90, height=16, font=(
              'Verdana 15 bold'))
              self.lista_locacoes.place(x=30, y=370)
              self.scrollbar_locacoes = Scrollbar(self )
              self.lista_locacoes.configure(yscrollcommand=self.scrollbar_veiculos.set)
              self.scrollbar_locacoes.configure(command=self.lista_veiculos.yview)
              self.scrollbar_locacoes.place(x=1293, y=370, relheight=0.22)
              self.botao_selecionar_locacao = Button(self, text="Selecionar \n locacao", width=10, height=5, bg='#ffdfba', fg='black', font=(
              'Verdana 15 bold'))
              self.botao_selecionar_locacao.place(x=1135, y=190)

       def update_list(self):
              try:
                     self.lista_locacoes.delete(0, END)
                     for item in self.dao.view():
                            self.lista_locacoes.insert(END, item)
              except Exception:
                     print('Erro na lista clientes.')
    
    
       def get_items(self):
              self.cliente.nome = self.nome_entry.get()
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


       def get_items(self):
              self.locacao

       def run(self):
              self.mainloop()

#DevolveVeiculo().run()