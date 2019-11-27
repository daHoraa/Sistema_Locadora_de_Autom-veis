from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, END, Toplevel
from veiculoDAO import VeiculoDAO
from veiculo import Veiculo
import tkinter.messagebox
import datetime


class CadastroVeiculo(Toplevel):
    '''Classe interface cadastrar veiculo'''

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        self.veiculo = Veiculo()
        self.dao = VeiculoDAO()

        self.geometry('1500x850+0+0')
        self.title('Cadastro de veiculos')
        self.resizable(0, 0)  # impede de maximizar
        self.configure(background='#c9c9ff')

        self.heading = Label(self, text="Cadastrar veiculos", bg='#c9c9ff', fg='white', font=(
            'Verdana 20 bold'))
        self.heading.place(x=650, y=0)

        # marca =========================================================================
        self.marca = Label(self, text="Marca do veículo :", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.marca.place(x=10, y=70)
        self.marca_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.marca_entry.place(x=300, y=70)

        # modelo =========================================================================
        self.modelo = Label(self, text="Modelo:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.modelo.place(x=10, y=120)
        self.modelo_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.modelo_entry.place(x=300, y=120)

        # ano =========================================================================
        self.ano = Label(self, text="Ano:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.ano.place(x=10, y=170)
        self.ano_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.ano_entry.place(x=300, y=170)

        # cor =========================================================================
        self.cor = Label(self, text="Cor:", bg='#c9c9ff', fg='white',  font=(
            'Verdana 15 bold'))
        self.cor.place(x=10, y=220)
        self.cor_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.cor_entry.place(x=300, y=220)
        # self.cor_entry.insert(END, datetime.date.today())

        # tanque =========================================================================
        self.tanque = Label(self, text="Capacidade do tanque:", bg='#c9c9ff', fg='white',  font=(
            'Verdana 15 bold'))
        self.tanque.place(x=10, y=270)
        self.tanque_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.tanque_entry.place(x=300, y=270)
        self.tanque_entry.insert(END, "litros")

        # combustivel =========================================================================
        self.combustivel = Label(self, text="Tipo de Combustível:", bg='#c9c9ff', fg='white',  font=(
            'Verdana 15 bold'))
        self.combustivel.place(x=10, y=320)
        self.combustivel_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.combustivel_entry.place(x=300, y=320)

        # consumo cidade =========================================================================
        self.consumo_cidade = Label(self, text="Consumo na cidade:", bg='#c9c9ff', fg='white',  font=(
            'Verdana 15 bold'))
        self.consumo_cidade.place(x=10, y=370)
        self.consumo_cidade_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.consumo_cidade_entry.place(x=300, y=370)

        self.consumo_cidade_entry.insert(END, "l/km")

        self.consumo_estrada = Label(self, text="Consumo na estrada:", bg='#c9c9ff', fg='white',  font=(
            'Verdana 15 bold'))
        self.consumo_estrada.place(x=10, y=420)
        self.consumo_estrada_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.consumo_estrada_entry.place(x=300, y=420)
        self.consumo_estrada_entry.insert(END, "l/km")

        self.tempo_0_100 = Label(self, text="Tempo de 0km/h a 100km/h:", bg='#c9c9ff', fg='white',  font=(
            'Verdana 15 bold'))
        self.tempo_0_100.place(x=10, y=470)
        self.tempo_0_100_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.tempo_0_100_entry.place(x=300, y=470)

        self.chassi = Label(self, text="Chassi:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.chassi.place(x=10, y=520)
        self.chassi_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.chassi_entry.place(x=300, y=520)

        self.placa = Label(self, text="Placa:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.placa.place(x=10, y=570)
        self.placa_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.placa_entry.place(x=300, y=570)

        self.tamanho_pneu = Label(self, text="Tamanho do pneu:", bg='#c9c9ff', fg='white',  font=(
            'Verdana 15 bold'))
        self.tamanho_pneu.place(x=10, y=620)
        self.tamanho_pneu_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.tamanho_pneu_entry.place(x=300, y=620)

        self.som = Label(self, text="Som:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.som.place(x=10, y=670)
        self.som_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.som_entry.place(x=300, y=670)

        self.valor_diaria = Label(self, text="valor da diária:", bg='#c9c9ff', fg='white', font=(
            'Verdana 15 bold'))
        self.valor_diaria.place(x=10, y=720)
        self.valor_diaria_entry = Entry(self, width=20, font=(
            'Verdana 15 bold'))
        self.valor_diaria_entry.place(x=300, y=720)
        self.valor_diaria_entry.insert(END, 'R$ ')

        # BOTAO LIMPAR  =========================================================================
        self.botao_limpar = Button(self, text="Limpar", width=31, height=1, bg='#ffdfba', fg='black', font=(
            'Verdana 15 bold'), command=self.clear_all)
        self.botao_limpar.place(x=600, y=700)

        self.botao_cadastrar = Button(self, text="Cadastrar", width=62, height=1, bg='#baffc9', fg='black', font=(
            'Verdana 15 bold'), command=self.get_items)
        self.botao_cadastrar.place(x=600, y=650)

        self.botao_sair = Button(self, text="Sair", width=30, height=1, bg='#ffb3ba', fg='black', font=(
            'Verdana 15 bold'), command=self.close)
        self.botao_sair.place(x=1048, y=700)

        self.veiculo_box = Listbox(self, width=63, height=20, font=(
            'Verdana 15 bold'))
        self.veiculo_box.place(x=600, y=120)

        self.scrollbar_veiculo = Scrollbar(self)
        self.veiculo_box.configure(yscrollcommand=self.scrollbar_veiculo.set)
        self.scrollbar_veiculo.configure(command=self.veiculo_box.yview)
        self.scrollbar_veiculo.place(
            x=1485, y=120, relheight=0.62, anchor='ne')

        self.pesquisar_veiculo = Label(self, text="Lista de veiculos Cadastrados:", bg='#c9c9ff',  font=(
            'Verdana 15 bold'))
        self.pesquisar_veiculo.place(x=900, y=65)

        self.view_command()

    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.veiculo_box.delete(0, END)
            for r in rows:
                self.veiculo_box.insert(END, r)
        except Exception as e:
            print(e)


    def get_items(self):
        self.veiculo.marca = self.marca_entry.get()
        self.veiculo.modelo = self.modelo_entry.get()
        self.veiculo.ano = self.ano_entry.get()
        self.veiculo.cor = self.cor_entry.get()
        self.veiculo.tanque = self.tanque_entry.get()
        self.veiculo.combustivel = self.combustivel_entry.get()
        self.veiculo.consumo_cidade = self.consumo_cidade_entry.get()
        self.veiculo.consumo_estrada = self.consumo_estrada_entry.get()
        self.veiculo.tempo_0_100 = self.tempo_0_100_entry.get()
        self.veiculo.chassi = self.chassi_entry.get()
        self.veiculo.placa = self.placa_entry.get()
        self.veiculo.tamanho_pneu = self.tamanho_pneu_entry.get()
        self.veiculo.som = self.som_entry.get()
        self.veiculo.valor_diaria = self.valor_diaria_entry.get()

        if(self.veiculo.marca == '' or self.veiculo.modelo == '' or self.veiculo.ano == '' or self.veiculo.cor == '' or self.veiculo.tanque == '' or self.veiculo.combustivel == '' or self.veiculo.consumo_cidade == '' or self.veiculo.consumo_estrada == '' or self.veiculo.tempo_0_100 == '' or self.veiculo.chassi == '' or self.veiculo.placa == '' or self.veiculo.tamanho_pneu == '' or self.veiculo.som == '' or self.veiculo.valor_diaria == ''):
            tkinter.messagebox.showinfo(
                "Aviso:", "POR FAVOR PREENCHER TODOS OS CAMPOS!")
        else:
            try:
                self.veiculo.tanque = float(self.veiculo.tanque)
                self.veiculo.consumo_cidade = float(
                    self.veiculo.consumo_cidade)
                self.veiculo.consumo_estrada = float(
                    self.veiculo.consumo_estrada)
                self.veiculo.tempo_0_100 = float(self.veiculo.tempo_0_100)
                self.veiculo.valor_diaria = float(self.veiculo.valor_diaria)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'Os campos tamanho do tanque, Consumo na cidade, consumo ma estrada, tempo_0_100 e valor da diária devem ser preenchidos com números!')
            else:
                try:
                    self.dao.insert(self.veiculo)
                except Exception as e:
                    print(e)
                else:
                    tkinter.messagebox.showinfo(
                        'Aviso!', 'Cadastro Realizado com Sucesso!')
                    self.clear_all()
                    self.view_command()

    def clear_all(self):
        self.marca_entry.delete(0, END)
        self.modelo_entry.delete(0, END)
        self.ano_entry.delete(0, END)
        self.cor_entry.delete(0, END)
        self.tanque_entry.delete(0, END)
        self.tanque_entry.insert(END, "litros")

        self.combustivel_entry.delete(0, END)

        self.consumo_cidade_entry.delete(0, END)
        self.consumo_cidade_entry.insert(END, "l/km")

        self.consumo_estrada_entry.delete(0, END)
        self.consumo_estrada_entry.insert(END, "l/km")

        self.tempo_0_100_entry.delete(0, END)
        self.tempo_0_100_entry.insert(END, "segundos")

        self.chassi_entry.delete(0, END)
        self.placa_entry.delete(0, END)
        self.tamanho_pneu_entry.delete(0, END)
        self.som_entry.delete(0, END)
        self.valor_diaria_entry.delete(0, END)
        self.valor_diaria_entry.insert(END, 'R$ ')

    def close(self):
        self.dao.close()
        self.destroy()

    def run(self):
        self.mainloop()


#CadastroVeiculo().run()
