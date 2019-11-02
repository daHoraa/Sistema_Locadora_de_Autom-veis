import sys

# veiculo import Veiculos, Disponivel
#from notebook import Notebook, Note

class Menu:
    '''Mostra um menu e aciona as ações apropriadas com base
    nas opções escolhidas.'''
    def __init__(self):
        #self.veiculos = Veiculos()
        #self.notebook = Notebook()
        self.choices = {
            "1": self.mostrar_veiculos,
            "2": self.buscar_veiculos,
            "3": self.alugar_veiculo,
            "4": self.devolver_veiculo,
            "5": self.gerenciar_clientes,
            "0": self.quit
        }
    def display_menu(self):
        print("""
        Notebook Menu
    
        1. Mostrar todos os veiculos disponíveis
        2. Buscar Veiculo
        3. Alugar veiculo
        4. Devolver veiculo
        5. Gerenciar clientes
        0. Sair
        """)
    def run(self):
        '''Mostra o menu e aciona a opção escolhida.'''
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} não é uma opção válida".format(choice))

    def mostrar_veiculos(self, veiculos=None):
        '''if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
        '''
        pass
    def buscar_veiculos(self):
        '''
        term = input("Buscar por: ")
        notes = self.notebook.search(term)
        self.show_notes(notes)
        '''
        pass
    def alugar_veiculo(self):
        '''memo = input("Entre com a anotação: ")
        self.notebook.new_note(memo)
        print("Sua anotação foi adicionada.")
        '''
        pass
    def devolver_veiculo(self):
        '''id = input("Entre com o id da anotação: ")
        memo = input("Entre com a anotação: ")
        tags = input("Entre com as tags: ")
        if memo:
            self.notebook.modify_memo(int(id), memo)
        if tags:
            self.notebook.modify_tags(int(id), tags)
        ''' 
        pass
    def quit(self):
        print("Obrigado por usar nosso sitema!")
        sys.exit(0)

    def gerenciarclientes():
        
if __name__ == "__main__":
    Menu().run()
