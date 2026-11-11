from Classes.Classe_Base import Animal
class Passaro(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade, especie)

    def miar(self):
        print(f"{self.nome} piou: Piu piu!")