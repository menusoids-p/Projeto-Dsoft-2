
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

def calcula_pontos_regra_simples (lista):
    saida = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for numero in lista:
        saida[numero] += numero
    
    return saida

def calcula_pontos_soma (lista):
    s = 0
    for num in lista:
        s += num
    return s

def calcula_pontos_sequencia_baixa (lista):

    l_ordem = []

    for num in lista:
        if num not in l_ordem:
            l_ordem.append(num)
    
    l_ordem = sorted(l_ordem)

    if len(l_ordem)<4:
        return 0

    for i in range(len(l_ordem) - 3):

        cond1 = l_ordem[i+1] == l_ordem[i] + 1 and l_ordem[i+2] == l_ordem[i] + 2 and l_ordem[i+3] == l_ordem[i] + 3
        if cond1:
            return 15
    
    return 0

def calcula_pontos_sequencia_alta(lista):
    
    l_ordem = []

    for num in lista:
        if num not in l_ordem:
            l_ordem.append(num)

    
    if len(l_ordem)<5:
        return 0

    l_ordem = sorted(l_ordem)

    for i in range(len(l_ordem)-1):
        proximo = l_ordem[i] + 1
        if l_ordem[i+1] != proximo:
            return 0
    return 30

def calcula_pontos_full_house(lista):
    l_ordem = sorted(lista)

    cond1 = l_ordem[0] == l_ordem[1] and l_ordem[2] == l_ordem[3] == l_ordem[4] and l_ordem[0] != l_ordem[3]
    cond2 = l_ordem[3] == l_ordem[4] and l_ordem[0] == l_ordem[1] == l_ordem[2] and l_ordem[0] != l_ordem[3]

    if cond1 or cond2:
        s = 0 
        for num in l_ordem:
            s += num
        return s
    else:
        return 0 
    
def calcula_pontos_quadra (lista):

    l_ordem = sorted(lista)

        
    for i in range(len(l_ordem)-3):
        
        cond = l_ordem[i] == l_ordem[i+1] == l_ordem[i+2] == l_ordem[i+3] 

        if cond:
            s = 0
            for num in l_ordem:
                s += num
            return s
    
    return 0

def calcula_pontos_quina (lista):

    l_ordem = sorted(lista)

        
    for i in range(len(l_ordem)-4):
        
        cond = l_ordem[i] == l_ordem[i+1] == l_ordem[i+2] == l_ordem[i+3] == l_ordem[i+4]

        if cond:
           return 50  
    return 0

def calcula_pontos_regra_avancada (lista):
   
    return {
    'cinco_iguais': calcula_pontos_quina(lista),
    'full_house': calcula_pontos_full_house(lista),
    'quadra': calcula_pontos_quadra(lista) ,
    'sem_combinacao':calcula_pontos_soma(lista) ,
    'sequencia_alta': calcula_pontos_sequencia_alta(lista) ,
    'sequencia_baixa': calcula_pontos_sequencia_baixa(lista)
    }

def faz_jogada(dados, categoria, cartela_de_pontos):

    numeros = ['1','2','3','4','5','6']
    if categoria in numeros:
        categoria = int(categoria)
    
    if categoria in cartela_de_pontos['regra_simples']:
        
        pontos = calcula_pontos_regra_simples(dados)
        
        cartela_de_pontos['regra_simples'][categoria] = pontos[categoria]

    
    elif categoria in cartela_de_pontos['regra_avancada']:
       
        pontos = calcula_pontos_regra_avancada(dados)
        
        cartela_de_pontos['regra_avancada'][categoria] = pontos[categoria]

    
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)