from funcoes import *

rolados = rolar_dados(5)
guardados = []

cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

def rodada(cartela, rolados, guardados):
    contador_rolagem = 0

    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    decisao = input()

    while decisao != '0':
        
        if decisao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())

            funcao = guardar_dado(rolados, guardados, indice)
            rolados = funcao[0]
            guardados = funcao[1]

            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            decisao = input()

        elif decisao == '2':
            
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())

            funcao = remover_dado(rolados, guardados, indice)
            rolados = funcao[0]
            guardados = funcao[1]

            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            decisao = input() 


        elif decisao == '3':
            if contador_rolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                rolados = rolar_dados(len(rolados))
                contador_rolagem += 1

            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            decisao = input()

        elif decisao == '4':
            imprime_cartela(cartela)

            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            decisao = input()

        else:
            print("Opção inválida. Tente novamente.")
            decisao = input()
        

    dados = rolados + guardados

    print("Digite a combinação desejada:")
    categoria = input()

    teste = verifica_categoria(categoria, cartela)

    while teste == 1 or teste == 0:
        if teste == 1:
            print("Essa combinação já foi utilizada.")
            categoria = input()

        elif teste == 0:
            print("Combinação inválida. Tente novamente.")
            categoria = input()
        teste = verifica_categoria(categoria, cartela)

    faz_jogada(dados, categoria, cartela)


    return cartela

# Programa principal
conta_rodada = 0

imprime_cartela(cartela)
print(f'Dados rolados: {rolados}')
print(f'Dados guardados: {guardados}')

while conta_rodada < 12:
    cartela = rodada(cartela, rolados, guardados)
    
    rolados = rolar_dados(5)
    guardados = []

    if conta_rodada != 11:
        print(f'Dados rolados: {rolados}')
        print(f'Dados guardados: {guardados}')
    
    conta_rodada += 1

# Cálculo da pontuação final
pontuacao = 0
pontos_regras_simples = 0

for regra, valores in cartela.items():
    for pontos in valores.values():
        pontuacao += pontos
        if regra == 'regra_simples':
            pontos_regras_simples += pontos

if pontos_regras_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")
