#  Sistema de Gerenciamento de Clínica Veterinária



##  Integrantes

- Pietro
- Murilo V.
- Henrique
- Guilherme

**Turma:** 2922

##  Classes do Sistema

O projeto é composto por quatro classes principais:

- **Animal (Classe base):** Armazena as informações gerais dos animais, como nome, idade e nome do tutor.
- **Cachorro (Classe filha):** Herda as características de Animal e possui atributos e métodos específicos para cachorros.
- **Gato (Classe filha):** Herda as características de Animal e possui atributos e métodos específicos para essa classe.
- **Pássaro (Classe filha):** Herda as características de animal e possui atributos e métodos específicos para essa classe.
- **Clinica (Classe gerenciadora):** Responsável por armazenar e gerenciar a lista de animais cadastrados.

### Diagrama de Classes

```text
                 ┌──────────────────┐
                 │      Animal      │
                 ├──────────────────┤
                 │ - nome           │
                 │ - idade          │
                 │ - tutor          │
                 ├──────────────────┤
                 │ + __str__()      │
                 │ + emitir_som()   │
                 └────────┬─────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
 ┌────────▼────────┐ ┌────▼──────────┐ ┌──▼──────────────┐
 │    Cachorro     │ │     Gato      │ │     Passaro     │
 ├─────────────────┤ ├───────────────┤ ├─────────────────┤
 │ - raca          │ │ - pelagem     │ │ - especie       │
 ├─────────────────┤ ├───────────────┤ ├─────────────────┤
 │ + emitir_som()  │ │ + emitir_som()│ │ + emitir_som()  │
 │ + brincar()     │ │ + arranhar()  │ │ + voar()        │
 └─────────────────┘ └───────────────┘ └─────────────────┘


                 ┌──────────────────┐
                 │      Clinica     │
                 ├──────────────────┤
                 │ - animais        │
                 ├──────────────────┤
                 │ + cadastrar()    │
                 │ + listar()       │
                 │ + buscar()       │
                 └──────────────────┘
```

## ️ Conceitos de POO Aplicados

**Encapsulamento:** Os atributos das classes são protegidos por atributos privados, e seu acesso é realizado por meio de getters e setters ou propriedades. Alguns setters possuem validações para impedir dados inválidos.

**Herança:** As classes Cachorro, Gato e Pássaro herdam os atributos e métodos da classe Animal, utilizando `super().__init__()` para chamar o construtor da classe base.

**Polimorfismo:** O método `emitir_som()` é sobrescrito nas classes filhas, apresentando comportamentos diferentes para cada tipo de animal.


##  Como Executar o Projeto

1. Clone o repositório do GitHub.
2. Abra a pasta do projeto no PyCharm.
3. Execute o arquivo `main.py`.
4. Utilize o menu apresentado no terminal para navegar pelas opções.
ínica veterinária, aplicando os conceitos de Programação Orientada a Objetos e praticando o trabalho em equipe por meio do Git e GitHub.