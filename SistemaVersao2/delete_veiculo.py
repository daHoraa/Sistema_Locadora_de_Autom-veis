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
        

        self.nome_tela = Label(self, text="Deletar Veiculos", bg='#c9c9ff', fg='white', font=(
            'Verdana 40 bold'))
        self.nome_tela.place(x=400, y=0)


        self.id = Label(self, text="Id:", bg='#c9c9ff', font=(
            'Verdana  15 bold'))
        self.id.place(x=10, y=70)
        self.id_entry = Entry(self, width=35, font=(
            'Verdana  15 bold'))
        self.id_entry.place(x=300, y=70)

        # marca ========================================================================= 
        self.marca = Label(self, text="Marca do veículo :", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.marca.place(x=10, y=70)
        self.marca_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.marca_entry.place(x=300, y=70)
        # modelo ========================================================================= 
        self.modelo = Label(self , text="Modelo:", bg='#c9c9ff',fg='white', font=(
        'Verdana 15 bold'))
        self.modelo.place(x=10, y=120)
        self.modelo_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.modelo_entry.place(x=300, y=120)
        # ano ========================================================================= 
        self.ano = Label(self , text="Ano:", bg='#c9c9ff',fg='white', font=(
        'Verdana 15 bold'))
        self.ano.place(x=10, y=170)
        self.ano_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.ano_entry.place(x=300, y=170)
        # cor ========================================================================= 
        self.cor = Label(self , text="Cor:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.cor.place(x=10, y=220)
        self.cor_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.cor_entry.place(x=300, y=220)
        # tanque ========================================================================= 
        self.tanque = Label(self , text="Capacidade do tanque:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.tanque.place(x=10, y=270)
        self.tanque_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.tanque_entry.place(x=300, y=270)
        # combustivel ========================================================================= 
        self.combustivel = Label(self , text="Tipo de Combustível:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.combustivel.place(x=10, y=320)
        self.combustivel_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.combustivel_entry.place(x=300, y=320)
        # consumo cidade ========================================================================= 
        self.consumo_cidade = Label(self , text="Consumo na cidade:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.consumo_cidade.place(x=10, y=370)
        self.consumo_cidade_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.consumo_cidade_entry.place(x=300, y=370)
        # consumo estrada ========================================================================= 
        self.consumo_estrada = Label(self , text="Consumo na estrada:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.consumo_estrada.place(x=10, y=420)
        self.consumo_estrada_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.consumo_estrada_entry.place(x=300, y=420)
        # tempo 0 a 100 ========================================================================= 
        self.tempo_0_100 = Label(self , text="Tempo de 0km/h a 100km/h:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.tempo_0_100.place(x=10, y=470)
        self.tempo_0_100_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.tempo_0_100_entry.place(x=300, y=470)
        # chassi ========================================================================= 
        self.chassi = Label(self , text="Chassi:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.chassi.place(x=10, y=520)
        self.chassi_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.chassi_entry.place(x=300, y=520)
        # placa ========================================================================= 
        self.placa = Label(self , text="Placa:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.placa.place(x=10, y=570)
        self.placa_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.placa_entry.place(x=300, y=570)
        # tamanho pneu ========================================================================= 
        self.tamanho_pneu = Label(self , text="Tamanho do pneu:", bg='#c9c9ff', fg='white',  font=(
        'Verdana 15 bold'))
        self.tamanho_pneu.place(x=10, y=620)
        self.tamanho_pneu_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.tamanho_pneu_entry.place(x=300, y=620)
        # som ========================================================================= 
        self.som = Label(self , text="Som:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.som.place(x=10, y=670)
        self.som_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.som_entry.place(x=300, y=670)
        # valor diaria ========================================================================= 
        self.valor_diaria = Label(self , text="valor da diária:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.valor_diaria.place(x=10, y=720)
        self.valor_diaria_entry = Entry(self , width=35, font=(
        'Verdana 15 bold'))
        self.valor_diaria_entry.place(x=300, y=720)


        self.botao_limpar = Button(self, text="Limpar", width= 15, height=1, bg='#ffdfba', fg='black', font=(
            'Verdana  15 bold'), command=self.clear_all)
        self.botao_limpar.place(x=800, y=700)

        self.botao_deletar = Button(master, text="Deletar", width=37, height=1, bg='#baffc9', fg='black', font=(
            'Verdana  15 bold'), command=self.delete)
        self.botao_deletar.place(x=800, y=650)

        self.botao_sair = Button(self, text="Sair", width= 15, height=1, bg='#ffb3ba', fg='black', font=(
            'Verdana  15 bold'), command=self.close)
        self.botao_sair.place(x=1070, y=700)

        self.veiculo_box = Listbox(self, width=38, height=20, font=(
            'Verdana  15 bold'))
        self.veiculo_box.place(x=800, y=120)

        self.scrollbar_veiculo = Scrollbar(self, )
        self.veiculo_box.configure(yscrollcommand=self.scrollbar_veiculo.set)
        self.scrollbar_veiculo.configure(command=self.veiculo_box.yview)
        self.scrollbar_veiculo.place(
            x=1340, y=120, relheight=0.62, anchor='ne')

        self.pesquisar_veiculo = Label(self, text="Pesquisar Veiculo:", bg='#c9c9ff', font=(
            'Verdana  15 bold'))
        self.pesquisar_veiculo.place(x=780, y=70)

        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index,
                              mode: self.update_list())
        self.search_entry = Entry(self, textvariable=self.search_var, width=20, font=(
            'Verdana  15 bold'))
        self.search_entry.place(x=1010, y=70)
        self.update_list()

        self.veiculo_box.bind('<<ListboxSelect>>', self.selecionar_linha)
       
    def selecionar_linha(self, event):
        '''Função para responder ao click do mouse na lista de veiculos, as informações da lista são
        carregadas nas entradas de dados na tela.'''
        if self.veiculo_box.curselection():
              self.clear_all()
              index = self.veiculo_box.curselection()[0]
              self.selected = self.veiculo_box.get(index)
              self.id_entry.insert(END, self.selected[0])
              self.marca_entry.insert(END, self.selected[1])
              self.modelo_entry.insert(END, self.selected[2])
              self.ano_entry.insert(END, self.selected[3])
              self.cor_entry.insert(END, self.selected[4])
              self.tanque_entry.insert(END, self.selected[5])
              self.combustivel_entry.insert(END, self.selected[6])
              self.consumo_cidade_entry.insert(END, self.selected[7])
              self.consumo_estrada_entry.insert(END, self.selected[8])
              self.tempo_0_100_entry.insert(END, self.selected[9])
              self.chassi_entry.insert(END, self.selected[10])
              self.placa_entry.insert(END, self.selected[11])
              self.tamanho_pneu_entry.insert(END, self.selected[12])
              self.som_entry.insert(END, self.selected[13])
              self.valor_diaria_entry.insert(END, self.selected[14])



    def update_list(self):
        '''Função para atualizar a lista, usado quando o usuário pesquisar pelo nome de algum veiculo
        para ver se o mesmo está registrado no estoque'''
        try:
            self.veiculo_box.delete(0, END)
            for item in self.dao.view():
                if str(self.search_var.get()).lower() in str(item).lower():
                    self.veiculo_box.insert(END, item)
        except Exception:
            tkinter.messagebox.showinfo(
                "Aviso:", "Erro ao buscar as informações do veiculo!")

    def delete(self):
        '''Função para deletar o veiculo do banco de dados'''
        try:
            self.dao.delete(self.id_entry.get())
        except Exception:
             tkinter.messagebox.showinfo(
                        'Aviso!', 'Erro ao acessar o banco de dados.')
        else:
            tkinter.messagebox.showinfo(
                'Aviso!', 'veiculo Excluido com Sucesso!')
            self.clear_all()
            self.update_list()

    def clear_all(self):
       '''Função para limpar todas as entradas de dados.'''
       self.id_entry.delete(0, END)
       self.marca_entry.delete(0, END)
       self.modelo_entry.delete(0, END)
       self.ano_entry.delete(0, END)
       self.cor_entry.delete(0, END)
       self.tanque_entry.delete(0, END)
       self.combustivel_entry.delete(0, END)
       self.consumo_cidade_entry.delete(0, END)
       self.consumo_estrada_entry.delete(0, END)
       self.tempo_0_100_entry.delete(0, END)
       self.chassi_entry.delete(0, END)
       self.placa_entry.delete(0, END)
       self.tamanho_pneu_entry.delete(0, END)
       self.som_entry.delete(0, END)
       self.valor_diaria_entry.delete(0, END)

    def close(self):
        '''Função para fechar a tela, fecha a conexão com o banco de dados e destroi a janela atual.'''
        self.dao.close()
        self.destroy()

    def run(self):
        '''Função para chamar a tela.'''
        self.mainloop()

#DeleteVeiculo().run()
