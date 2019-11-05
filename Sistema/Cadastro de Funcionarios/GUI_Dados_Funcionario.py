from tkinter import *

class Gui():
    def __init__(self):
        
        self.window = Tk()
        self.window.wm_title("Cadastro de Funcionarios")

        self.txtNacionalidade = StringVar()
        self.txtTipo_Documento = StringVar()
        self.txtCPF = StringVar()
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtGenero = StringVar()
        self.txtTelefone = StringVar()
        self.txtNascimento = StringVar()
        self.txtInstrucao = StringVar()
        
        self.lblnacionalidade = Label(self.window, text="Nacionalidade")
        self.lbltipo_documento = Label(self.window, text="Tipo de Documento")
        self.lblcpf = Label(self.window, text="CPF")
        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="Email")
        self.lblgenero = Label(self.window, text="Gênero")
        self.lbltelefone = Label(self.window, text="Telefone")
        self.lblnascimento = Label(self.window, text="Data de Nascimento")
        self.lblinstrucao = Label(self.window, text="Grau de Instrução")
        
        self.entNacionalidade = Entry(self.window, textvariable=self.txtNacionalidade)
        self.entTipo_Documento = Entry(self.window, textvariable=self.txtTipo_Documento)
        self.entGenero = Entry(self.window, textvariable=self.txtGenero)
        self.entTelefone= Entry(self.window, textvariable=self.txtTelefone)
        self.entNome = Entry(self.window, textvariable=self.txtNome)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF)
        self.entNascimento = Entry(self.window, textvariable=self.txtNascimento)
        self.entInstrucao = Entry(self.window, textvariable=self.txtInstrucao)
        
        self.listFuncionarios = Listbox(self.window, width=100)
        self.scrollFuncionarios = Scrollbar(self.window)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Continuar")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

    def configure_layout(self):
        
        #Associando os objetos a grid da janela...
        self.lblnacionalidade.grid(row=0,column=0)
        self.lbltipo_documento.grid(row=1,column=0)
        self.lblcpf.grid(row=2, column=0)
        self.lblgenero.grid(row=3,column=0)
        self.lbltelefone.grid(row=4,column=0)
        self.lblnome.grid(row=5,column=0)
        self.lblsobrenome.grid(row=6,column=0)
        self.lblemail.grid(row=7,column=0)
        self.lblnascimento.grid(row=8,column=0)
        self.lblinstrucao.grid(row=9,column=0)
        
        self.entNacionalidade.grid(row=0, column=1)
        self.entTipo_Documento.grid(row=1, column=1)
        self.entCPF.grid(row=2, column=1)
        self.entGenero.grid(row=3, column=1)
        self.entTelefone.grid(row=4, column=1)
        self.entNome.grid(row=5, column=1)
        self.entSobrenome.grid(row=6, column=1)
        self.entEmail.grid(row=7, column=1)
        self.entNascimento.grid(row=8,column=1)
        self.entInstrucao.grid(row=9,column=1)
             
        self.listFuncionarios.grid(row=0, column=2, rowspan=10)
        self.scrollFuncionarios.grid(row=0, column=3, rowspan=10)
        self.btnViewAll.grid(row=10, column=0, columnspan=2)
        self.btnBuscar.grid(row=11, column=0, columnspan=2)
        self.btnInserir.grid(row=12, column=0, columnspan=2)
        self.btnUpdate.grid(row=13, column=0, columnspan=2)
        self.btnDel.grid(row=14, column=0, columnspan=2)
        self.btnClose.grid(row=15, column=0, columnspan=2)
        
        self.listFuncionarios.configure(yscrollcommand=self.scrollFuncionarios.set)
        self.scrollFuncionarios.configure(command=self.listFuncionarios.yview)

    def configure_sizes(self):
        "definindo o tamanho dos elementos"
        x_pad = 10
        y_pad = 6

        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=5, pady=5, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=5, pady=5, sticky='NS')
            else:
                child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        self.configure_layout()
        self.configure_sizes()
        self.window.mainloop()

Gui().run()