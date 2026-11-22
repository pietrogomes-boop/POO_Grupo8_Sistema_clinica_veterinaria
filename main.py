
from Classes.Classe_Gerenciadora import Clinica

from Classes.Classes_filhas.Classe_Cachorro import Cachorro
from Classes.Classes_filhas.Classe_gato import Gato
from Classes.Classes_filhas.Classe_Passaro import Passaro


# Criando a clínica
clinica = Clinica()

continuar = True

while continuar:

    print("\n  -------------------------------")
    print(" |       CLINICA VETERINARIA     |")
    print(" |                               |")
    print(" | 1 - Cadastrar animal          |")
    print(" | 2 - Listar animais            |")
    print(" | 3 - Buscar animal             |")
    print(" | 4 - Emitir sons               |")
    print(" | 0 - Sair do programa          |")
    print("  -------------------------------")

    opcao = input("Escolha uma opção: ")

    match opcao:

        # CADASTRAR ANIMAL
        case "1":

            print("\n  ---------------------")
            print(" | 1 - Cachorro        |")
            print(" | 2 - Gato            |")
            print(" | 3 - Passaro         |")
            print(" | 0 - Voltar          |")
            print("  ---------------------")

            animalesp = input("Informe a espécie do animal: ")

            match animalesp:

                case "1":
                    nome = input("Informe o nome do cachorro: ")
                    idade = int(input("Informe a idade (meses): "))
                    peso = float(input("Informe o peso (Kg): "))

                    animal = Cachorro(nome, idade, "Cachorro", peso)
                    clinica.cadastrar_animal(animal)

                case "2":
                    nome = input("Informe o nome do gato: ")
                    idade = int(input("Informe a idade (meses): "))
                    peso = float(input("Informe o peso (Kg): "))

                    animal = Gato(nome, idade, "Gato", peso)
                    clinica.cadastrar_animal(animal)

                case "3":
                    nome = input("Informe o nome do pássaro: ")
                    idade = int(input("Informe a idade (meses): "))
                    peso = float(input("Informe o peso (Kg): "))

                    animal = Passaro(nome, idade, "Passaro", peso)
                    clinica.cadastrar_animal(animal)

                case "0":
                    print("Voltando ao menu...")

                case _:
                    print("Espécie inválida!")

        # LISTAR ANIMAIS
        case "2":

            clinica.listar_animais()

        # BUSCAR ANIMAL
        case "3":

            nome = input("\nInforme o nome do animal que deseja buscar: ")

            clinica.buscar_animal(nome)

        # EMITIR SONS (POLIMORFISMO)
        case "4":

            print("\n===== SONS DOS ANIMAIS =====")
            clinica.emitir_sons()

        # SAIR
        case "0":

            print("\nEncerrando programa!")
            continuar = False

        # OPÇÃO INVÁLIDA
        case _:

            print("\nOpção inválida!")
