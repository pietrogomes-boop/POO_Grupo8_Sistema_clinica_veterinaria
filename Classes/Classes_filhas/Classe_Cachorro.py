from Classes.Classe_Base import Animal
class Cachorro(Animal):
    def __init__(self, nome, idade, especie, peso):
        super().__init__(nome, idade, especie, peso)


    def latir(self):
        print(f"{self.nome} latiu: Au au!")

