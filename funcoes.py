
import random

def rolar_dados(n):
    lista = []
    for i in range(n):
        x = random.randint(1,6)
        lista.append(x)
    return lista
