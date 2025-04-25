
import random

def rolar_dados(n):
    lista = []
    for i in range(n):
        x = random.randint(1,6)
        lista.append(x)
    return lista

def guardar_dado(rolados,guardados,indice):
    valor = rolados[indice]
    guardados.append(valor)

    del(rolados[indice])

    return [rolados, guardados]

def remover_dado(rolados,guardados,indice):
    valor = guardados[indice]
    rolados.append(valor)

    del(guardados[indice])

    return [rolados, guardados]


