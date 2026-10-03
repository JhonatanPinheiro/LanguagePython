cores = (                         # Cria uma tupla com 4 cores
    "vermelho",                   # Aparece 1 vez
    "azul",                       # Aparece 2 vezes
    "verde",                      # Aparece 1 vez
    "azul",                       # Aparece novamente
)

print(cores.count("vermelho"))    # Conta quantas vezes "vermelho" aparece → 1
print(cores.count("azul"))        # Conta quantas vezes "azul" aparece → 2
print(cores.count("verde"))       # Conta quantas vezes "verde" aparece → 1