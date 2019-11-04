from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button

class Gui():
    def __init__(self):
        '''Essa classe modela a interface gráfica
        da aplicação
        '''
        self.window = Tk()
        self.window.wm_title("Cadastro de Veiculos")

        self.txtMarca = StringVar()
        self.txtModelo = StringVar()
        self.txtAno = StringVar()
        self.txtCor = StringVar()
        self.txtTanque = StringVar()
        self.txtCombustivel = StringVar()
        self.txtConsumo_Cidade = StringVar()
        self.txtConsumo_Estrada = StringVar()
        self.txtTempo_0_100 = StringVar()
        self.txtChassi = StringVar()
        self.txtPlaca = StringVar()
        self.txtTamanho_Pneu = StringVar()
        self.txtSom = StringVar()
        self.txtValor_Diaria = StringVar()

        self.lblmarca = Label(self.window, text="Marca")
        self.lblmodelo = Label(self.window, text="Modelo")
        self.lblano = Label(self.window, text="Ano")
        self.lblcor = Label(self.window, text="Cor")
        self.lbltanque = Label(self.window, text="Tanque")
        self.lblcombustivel = Label(self.window, text="Tipo de combustível")
        self.lblconsumo_cidade = Label(self.window, text="Consumo na cidade")
        self.lblconsumo_estrada = Label(self.window, text="Consumo na estrada")
        self.lbltempo_0_100 = Label(self.window, text="Tempo de 0 a 100")
        self.lblchassi = Label(self.window, text="Chassi")
        self.lblplaca = Label(self.window, text="Placa")
        self.lbltamanho_pneu = Label(self.window, text="Tamanho do pneu")
        self.lblsom = Label(self.window, text="Som")
        self.lblvalor_diaria = Label(self.window, text="Valor da diária")


        self.entMarca = Entry(self.window, textvariable=self.txtMarca)
        self.entModelo = Entry(self.window, textvariable=self.txtModelo)
        self.entAno = Entry(self.window, textvariable=self.txtAno)
        self.entCor = Entry(self.window, textvariable=self.txtCor)
        
        self.entTanque = Entry(self.window, textvariable=self.txtTanque)
        self.entCombustivel = Entry(self.window, textvariable=self.txtCombustivel)
        self.entConsumo_Cidade = Entry(self.window, textvariable=self.txtConsumo_Cidade)
        self.entConsumo_Estrada = Entry(self.window, textvariable=self.txtConsumo_Estrada)

        self.entTempo_0_100 = Entry(self.window, textvariable=self.txtTempo_0_100)
        self.entChassi = Entry(self.window, textvariable=self.txtChassi)
        self.entPlaca = Entry(self.window, textvariable=self.txtPlaca)
        self.entTamanho_Pneu = Entry(self.window, textvariable=self.txtTamanho_Pneu)

        self.entSom = Entry(self.window, textvariable=self.txtSom)
        self.entValor_Diaria = Entry(self.window, textvariable=self.txtValor_Diaria)
        

        self.listVeiculos = Listbox(self.window, width=45)
        self.scrollVeiculos = Scrollbar(self.window)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

    def configure_layout(self):
        "Configurando os itens na janela em grid"
        
        #Associando os objetos a grid da janela...
        self.lblmarca.grid(row=0,column=0)
        self.lblmodelo.grid(row=1,column=0)
        self.lblano.grid(row=2,column=0)
        self.lblcor.grid(row=3, column=0)
        
        self.entMarca.grid(row=0, column=1)
        self.entModelo.grid(row=1, column=1)
        self.entAno.grid(row=2, column=1)
        self.entCor.grid(row=3, column=1)

        self.lbltanque.grid(row=0,column=2)
        self.lblcombustivel.grid(row=1,column=2)
        self.lblconsumo_cidade.grid(row=2,column=2)
        self.lblconsumo_estrada.grid(row=3, column=2)
        
        self.entTanque.grid(row=0, column=3)
        self.entCombustivel.grid(row=1, column=3)
        self.entConsumo_Cidade.grid(row=2, column=3)
        self.entConsumo_Estrada.grid(row=3, column=3)

        self.lbltempo_0_100.grid(row=4,column=2)
        self.lblchassi.grid(row=5,column=2)
        self.lblplaca.grid(row=6,column=2)
        self.lbltamanho_pneu.grid(row=7, column=2)
        
        self.entTempo_0_100.grid(row=4, column=3)
        self.entChassi.grid(row=5, column=3)
        self.entPlaca.grid(row=6, column=3)
        self.entTamanho_Pneu.grid(row=7, column=3)

        self.lblsom.grid(row=8,column=2)
        self.lblvalor_diaria.grid(row=9,column=2)
        
        self.entSom.grid(row=8, column=3)
        self.entValor_Diaria.grid(row=9, column=3)

        
        self.listVeiculos.grid(row=0, column=4, rowspan=10)#rowspan para fazer com que o objeto ocupe mais de uma linha.
        self.scrollVeiculos.grid(row=0, column=5, rowspan=10)
        self.btnViewAll.grid(row=4, column=0, columnspan=2)#columnspan para fazer com que o objeto ocupe mais de uma linha.
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        #Associando a Scrollbar com a Listbox...
        self.listVeiculos.configure(yscrollcommand=self.scrollVeiculos.set)
        self.scrollVeiculos.configure(command=self.listVeiculos.yview)

    def configure_sizes(self):
        "definindo o tamanho dos elementos"
        x_pad = 5
        y_pad = 3

        '''
        * Precisamos aplicar o padding para quase todos os 
        elementos, definir a largura dos botões e mais alguns
        pontos estéticos. Isso poderia ser feito manualmente,
        repetindo o código para todos os elementos. Todavia, 
        não vamos fazer assim.
        * Faremos a mudança de estilo da seguinte forma: Uma
        iteração por todos os elementos da janela, realizando
        as alterações conforme passamos pelos elementos.
        '''
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
        '''
        * padx e pady: Padding para o eixo X e Y do elemento. 
        É referente ao espaço entre a borda deste elemento e 
        a borda dos outros elementos da janela;
        * sticky: Indica em qual ponto da janela (norte – N, 
        sul – S, leste – E ou oeste W) o objeto estará ancorado. 
        Se você combinar o ponto leste e oeste (EW), o elemento 
        ocupará todo o espaço horizontal da coluna em que está 
        localizado. O mesmo ocorre se colocarmos NS (norte-sul), 
        o elemento ocupará todo o espaço vertical.
        * Para o ListBox e o ScrollBar, vamos definir padding zero 
        para que eles fiquem colados, parecendo que são apenas um elemento.
        '''

    def run(self):
        self.configure_layout()
        self.configure_sizes()
        self.window.mainloop()

                                                                                                        Gui().run()
