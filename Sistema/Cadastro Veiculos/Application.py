from telas import Tela_CadastroVeiculos
from dao import VeiculoDAO
from tkinter import END
from model import Veiculo

'''
Adaptado de:
https://github.com/brenordv/python-tutorial-tkinter-sqlite-01
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-01/
https://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-02/
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-03/
http://raccoon.ninja/pt/dev-pt/tutorial-aplicacao-em-python-sqlite-parte-04/
'''

class Controller:
    def __init__(self):
        self.gui = Gui()
        self.dao = VeiculoDAO()
        self.selected = None #cliente selecionado
        self.currentVeiculo = Veiculo()
    
    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.gui.listVeiculos.delete(0, END)
            for r in rows:
                self.gui.listVeiculos.insert(END, r)
        except Exception as e:
            print(e)

    def __fill_current_veiculo(self):
        self.currentVeiculo.marca = self.gui.txtMarca.get()
        self.currentVeiculo.modelo = self.gui.txtModelo.get()
        self.currentVeiculo.ano = self.gui.txtAno.get()
        self.currentVeiculo.cor = self.gui.txtCor.get()

        self.currentVeiculo.tanque = self.gui.txtTanque.get()
        self.currentVeiculo.combustivel = self.gui.txtCombustivel.get()
        self.currentVeiculo.consumo_cidade = self.gui.txtConsumo_Cidade.get()
        self.currentVeiculo.consumo_estrada = self.gui.txtConsumo_Estrada.get()


        self.currentVeiculo.tempo_0_100 = self.gui.txtTempo_0_100.get()
        self.currentVeiculo.chassi = self.gui.txtChassi.get()
        self.currentVeiculo.placa = self.gui.txtPlaca.get()
        self.currentVeiculo.tamanho_pneu = self.gui.txtTamanho_Pneu.get()
        self.currentVeiculo.som = self.gui.txtSom.get()
        self.currentVeiculo.valor_diaria = self.gui.txtValor_Diaria.get()
        
    def search_command(self):
        "método para buscar registros"
        self.gui.listVeiculos.delete(0, END)
        self.__fill_current_veiculo()
        try:
            rows = self.dao.search(self.currentVeiculo)
            for r in rows:
                self.gui.listVeiculos.insert(END, r)
        except Exception as e:
            print(e)
    
    def insert_command(self):
        "método para inserir registros"
        self.__fill_current_veiculo()
        self.dao.insert(self.currentVeiculo)
        self.view_command()

    def get_selected_row(self, event):
        "método que seleciona na listbox e popula os campos de input"
        if self.gui.listVeiculos.curselection():
            index = self.gui.listVeiculos.curselection()[0]        
            self.selected = self.gui.listVeiculos.get(index)
            self.gui.entMarca.delete(0, END)
            self.gui.entMarca.insert(END, self.selected[1])
            self.gui.entModelo.delete(0, END)
            self.gui.entModelo.insert(END, self.selected[2])
            self.gui.entAno.delete(0, END)
            self.gui.entAno.insert(END, self.selected[3])
            self.gui.entCor.delete(0, END)
            self.gui.entCor.insert(END, self.selected[4])

            self.gui.entTanque.delete(0, END)
            self.gui.entTanque.insert(END, self.selected[1])
            self.gui.entCombustivel.delete(0, END)
            self.gui.entCombustivel.insert(END, self.selected[2])
            self.gui.entConsumo_Cidade.delete(0, END)
            self.gui.entConsumo_Cidade.insert(END, self.selected[3])
            self.gui.entConsumo_Estrada.delete(0, END)
            self.gui.entConsumo_Estrada.insert(END, self.selected[4])

            self.gui.entTempo_0_100.delete(0, END)
            self.gui.entTempo_0_100.insert(END, self.selected[1])
            self.gui.entChassi.delete(0, END)
            self.gui.entChassi.insert(END, self.selected[1])
            self.gui.entPlaca.delete(0, END)
            self.gui.entPlaca.insert(END, self.selected[1])
            self.gui.entTamanho_Pneu.delete(0, END)
            self.gui.entTamanho_Pneu.insert(END, self.selected[1])

            self.gui.entSom.delete(0, END)
            self.gui.entSom.insert(END, self.selected[1])
            self.gui.entValor_Diaria.delete(0, END)
            self.gui.entValor_Diaria.insert(END, self.selected[1])

    def update_command(self):
        "método para atualizar registro"
        id = self.selected[0]
        self.__fill_current_veiculo()
        self.dao.update(id,self.currentVeiculo)
        self.view_command()

    def del_command(self):
        "método para remover registro"
        id = self.selected[0]
        self.dao.delete(id)
        self.view_command()

    def close_command(self):
        self.dao.close()
        self.gui.window.destroy()


    def start(self):
        self.gui.listVeiculos.bind('<<ListboxSelect>>', self.get_selected_row)
        #associando o comportamento à interface
        self.gui.btnViewAll.configure(command=self.view_command)
        self.gui.btnBuscar.configure(command=self.search_command)
        self.gui.btnInserir.configure(command=self.insert_command)
        self.gui.btnUpdate.configure(command=self.update_command)
        self.gui.btnDel.configure(command=self.del_command)
        self.gui.btnClose.configure(command=self.close_command)
        self.gui.run()

Controller().start()
