class Animal:
    def __init__(self, nome, idade, especie, peso):
        self.nome = nome
        self.__idade = idade
        self.__especie = especie
        self.peso = peso

    @property
    def idade(self):
        return self.__idade

    def alterar_idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválida")
        else:
            self.__idade = nova_idade

    @property
    def especie(self):
        return self.__especie

    def emitir_som(self):
        return "Som não identificado"

    def __str__(self):
        return f"Nome: {self.nome} / Idade: {self.idade} / Espécie: {self.especie}"
