from Classes.Classe_Base import Animal

class Passaro(Animal):
    """ Define as caracteristicas dos passaros"""
    def __init__(self, nome, idade, especie,peso):
        super().__init__(nome, idade, especie,peso)

    def emitir_som(self):
        return "Piu piu!"