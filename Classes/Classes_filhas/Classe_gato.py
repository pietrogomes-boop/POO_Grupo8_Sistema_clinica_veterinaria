from Classes.Classe_Base import Animal
class Gato(Animal):
    """Definir as caracteristicas dos gatos no veterinario"""
    def __init__(self, nome, idade, especie,peso):
        super().__init__(nome, idade, especie,peso)

    def emitir_som(self):
        return "Miau miau!"
