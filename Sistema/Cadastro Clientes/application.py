from telas import Tela_DadosPessoais
from dao import ClientDAO
from tkinter import END
from cliente import Client

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
        self.dao = ClientDAO()
        self.selected = None #cliente selecionado
        self.currentClient = Client()
    
    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.gui.listClientes.delete(0, END)
            for r in rows:
                self.gui.listClientes.insert(END, r)
        except Exception as e:
            print(e)

    def __fill_current_client(self):
        
        #dados pessoais

        self.currentClient.nacionalidade = self.gui.txtNacionalidade.get()
        self.currentClient.tipo_documento = self.gui.txtTipo_Documento.get()
        self.currentClient.nome = self.gui.txtNome.get()
        self.currentClient.sobrenome = self.gui.txtSobrenome.get()
        self.currentClient.email = self.gui.txtEmail.get()
        self.currentClient.cpf = self.gui.txtCPF.get()
        self.currentClient.genero = self.gui.txtGenero.get()
        self.currentClient.telefone = self.gui.txtTelefone.get()

        #dados da cnh
        self.currentClient.numero_cnh = self.gui.txtNumero_CNH.get()
        self.currentClient.numero_registro_cnh = self.gui.txtNumero_Registro_CNH.get()
        self.currentClient.data_validade_cnh = self.gui.txtData_Validade_CNH.get()
        self.currentClient.uf_cnh = self.gui.txtUf_CNH.get()
        self.currentClient.rg = self.gui.txtRG.get()
        self.currentClient.nascimento = self.gui.txtNascimento.get()

        #dados endereco
        self.currentClient.cep = self.gui.txtCEP.get()
        self.currentClient.logradouro = self.gui.txtLogradouro.get()
        self.currentClient.endereco = self.gui.txtEndereco.get()
        self.currentClient.numero_endereco = self.gui.txtNumero_Endereco.get()
        self.currentClient.complemento = self.gui.txtComplemento.get()
        self.currentClient.bairro = self.gui.txtBairro.get()
        self.currentClient.cidade = self.gui.txtCidade.get()
        self.currentClient.estado = self.gui.txtEstado.get()
        

    def search_command(self):
        "método para buscar registros"
        self.gui.listClientes.delete(0, END)
        self.__fill_current_client()
        try:
            rows = self.dao.search(self.currentClient)
            for r in rows:
                self.gui.listClientes.insert(END, r)
        except Exception as e:
            print(e)
    
    def insert_command(self):
        "método para inserir registros"
        self.__fill_current_client()
        self.dao.insert(self.currentClient)
        self.view_command()

    def get_selected_row(self, event):
        "método que seleciona na listbox e popula os campos de input"
        if self.gui.listClientes.curselection():
            index = self.gui.listClientes.curselection()[0]        
            self.selected = self.gui.listClientes.get(index)
            
            #dados pessoais 
            self.gui.entNacionalidade.delete(0, END)
            self.gui.entNacionalidade.insert(END, self.selected[1])
            self.gui.entTipo_Documento.delete(0, END)
            self.gui.entTipo_Documento.insert(END, self.selected[1])
            self.gui.entCPF.delete(0, END)
            self.gui.entCPF.insert(END, self.selected[4])
            self.gui.entNome.delete(0, END)
            self.gui.entNome.insert(END, self.selected[1])
            self.gui.entSobrenome.delete(0, END)
            self.gui.entSobrenome.insert(END, self.selected[2])
            self.gui.entEmail.delete(0, END)
            self.gui.entEmail.insert(END, self.selected[3])
            
            self.gui.entGenero.delete(0, END)
            self.gui.entGenero.insert(END, self.selected[4])
            self.gui.entTelefone.delete(0, END)
            self.gui.entTelefone.insert(END, self.selected[4])
            
            #dados cnh
            self.gui.entNumero_CNH.delete(0, END)
            self.gui.entNumero_CNH.insert(END, self.selected[4])
            self.gui.entNumero_Registro_CNH.delete(0, END)
            self.gui.entNumero_Registro_CNH.insert(END, self.selected[4])
            self.gui.entData_Validade_CNH.delete(0, END)
            self.gui.entData_Validade_CNH.insert(END, self.selected[4])
            self.gui.entUf_CNH.delete(0, END)
            self.gui.entUf_CNH.insert(END, self.selected[4])
            self.gui.entRG.delete(0, END)
            self.gui.entRG.insert(END, self.selected[4])
            self.gui.entNascimento.delete(0, END)
            self.gui.entNascimento.insert(END, self.selected[4])
            
            # dados endereco
            self.gui.entCep.delete(0, END)
            self.gui.entCep.insert(END, self.selected[4])
            self.gui.entLogradouro.delete(0, END)
            self.gui.entLogradouro.insert(END, self.selected[4])
            self.gui.entEndereco.delete(0, END)
            self.gui.entEndereco.insert(END, self.selected[4])
            self.gui.entNumero_Endereco.delete(0, END)
            self.gui.entNumero_Endereco.insert(END, self.selected[4])
            self.gui.entComplemento.delete(0, END)
            self.gui.entComplemento.insert(END, self.selected[4])
            self.gui.entBairro.delete(0, END)
            self.gui.entBairro.insert(END, self.selected[4])
            self.gui.entCidade.delete(0, END)
            self.gui.entCidade.insert(END, self.selected[4])
            self.gui.entEstado.delete(0, END)
            self.gui.entEstado.insert(END, self.selected[4])
            
    def update_command(self):
        "método para atualizar registro"
        id = self.selected[0]
        self.__fill_current_client()
        self.dao.update(id,self.currentClient)
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
        self.gui.listClientes.bind('<<ListboxSelect>>', self.get_selected_row)
        #associando o comportamento à interface
        self.gui.btnViewAll.configure(command=self.view_command)
        self.gui.btnBuscar.configure(command=self.search_command)
        self.gui.btnInserir.configure(command=self.insert_command)
        self.gui.btnUpdate.configure(command=self.update_command)
        self.gui.btnDel.configure(command=self.del_command)
        self.gui.btnClose.configure(command=self.close_command)
        self.gui.run()

Controller().start()
