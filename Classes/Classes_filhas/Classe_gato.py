from Classes.Classe_Base import Animal
class Gato(Animal):
    """Definir as caracteristicas dos gatos no veterinario"""
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade, especie)

    def miar(self):
        print(f"{self.nome} miou: Miau miau!")
