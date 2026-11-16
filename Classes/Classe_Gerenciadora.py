class Clinica:
    """essa clase defini as caracteristicas e especificacoes da clinica veterinaria"""
    def __init__(self):
        self.__animais = []

    def cadastrar_animal(self, animal):
        self.__animais.append(animal)
        print("Animal cadastrado com sucesso!")

    def listar_animais(self):
        if len(self.__animais) == 0:
            print("Nenhum animal cadastrado.")
        else:
            print("\n===== Animais cadastrados =====")
            for animal in self.__animais:
                print(animal)

    def buscar_animal(self, nome):
        encontrado = False

        for animal in self.__animais:
            if animal.nome.lower() == nome.lower():
                print(animal)
                encontrado = True

        if encontrado == False:
            print("Animal não encontrado.")

    def emitir_sons(self):
        if len(self.__animais) == 0:
            print("Nenhum animal cadastrado.")
        else:
            for animal in self.__animais:
                print(f"{animal.nome}: {animal.emitir_som()}")

    def __str__(self):
        return f"Total de animais cadastrados: {len(self.__animais)}"
