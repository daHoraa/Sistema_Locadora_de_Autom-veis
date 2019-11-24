from telas import Tela_CadastroFuncionario
from dao import FuncionarioDAO
from tkinter import END
from funcionario import Funcionario

class Controller:
    def __init__(self):
        self.gui = Gui()
        self.dao = FuncionarioDAO()
        self.selected = None #funcionario selecionado
        self.currentFuncionario = Funcionario()

    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.dao.view()
            self.gui.listFuncionarios.delete(0, END)
            for r in rows:
                self.gui.listFuncionarios.insert(END, r)
        except Exception as e:
            print(e)

    def __fill_current_funcionario(self):

        self.currentFuncionarioNacionalidade = self.gui.txtNacionalidade.get()
        self.currentFuncionarioTipo_documento = self.gui.txtTipo_Documento.get()
        self.currentFuncionarioCpf = self.gui.txtCPF.get()
        self.currentFuncionarioNome = self.gui.txtNome.get()
        self.currentFuncionarioSobrenome = self.gui.txtSobrenome.get()
        self.currentFuncionarioEmail = self.gui.txtEmail.get()
        self.currentFuncionarioGenero = self.gui.txtGenero.get()
        self.currentFuncionarioTelefone = self.gui.txtTelefone.get()
        self.currentFuncionarioNascimento = self.gui.txtNascimento.get()
        self.currentFuncionarioInstrucao = self.gui.txtInstrucao.get()

    def search_command(self):
        self.gui.listFuncionarios.delete(0, END)
        self.__fill_current_funcionario()
        try:
            rows = self.dao.search(self.currentFuncionario)
            for r in rows:
                self.gui.listFuncionarios.insert(END, r)
        except Exception as e:
            print(e)

    def insert_command(self):
        "método para inserir registros"
        self.__fill_current_Funcionario()
        self.dao.insert(self.currentFuncionario)
        self.view_command()

    def get_selected_row(self, event):
        "método que seleciona na listbox e popula os campos de input"
        if self.gui.listFuncionarios.curselection():
            index = self.gui.listFuncionarios.curselection()[0]        
            self.selected = self.gui.listFuncionarios.get(index)
            
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
            self.gui.entNascimento.delete(0, END)
            self.gui.entNascimento.insert(END, self.selected[1])
            self.gui.entInstrucao.delete(0, END)
            self.gui.entInstrucao.insert(END, self.selected[2])

    def update_command(self):
        "método para atualizar registro"
        id = self.selected[0]
        self.__fill_current_Funcionario()
        self.dao.update(id,self.currentFuncionario)
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
        self.gui.listFuncionarios.bind('<<ListboxSelect>>', self.get_selected_row)
        #associando o comportamento à interface
        self.gui.btnViewAll.configure(command=self.view_command)
        self.gui.btnBuscar.configure(command=self.search_command)
        self.gui.btnInserir.configure(command=self.insert_command)
        self.gui.btnUpdate.configure(command=self.update_command)
        self.gui.btnDel.configure(command=self.del_command)
        self.gui.btnClose.configure(command=self.close_command)
        self.gui.run()

Controller().start()