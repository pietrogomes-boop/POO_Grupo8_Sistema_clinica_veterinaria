from Classes.Classe_Base import Animal
class Cachorro(Animal):
    """ Classe para definir caracteristicas dos cachorro """
    def __init__(self, nome, idade, especie, peso):
        super().__init__(nome, idade, especie, peso)


    def emitir_som(self):
        return "Au au!"
