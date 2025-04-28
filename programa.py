
from funcoes import *

rolados = rolar_dados(6)
guardados = []

cartela= {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

def rodada(cartela, rolados, guardados):
    decisao = int(input( "Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))

    contador_rolagem = 0

    while decisao != 0:
        
        if decisao == 1:
            indice = int(input( "Digite o índice do dado a ser guardado (0 a 4):"))
            funcao = guardar_dado(rolados,guardados,indice)
            rolados = funcao[0]
            guardados = funcao[1]
            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')
        
        elif decisao == 2 and contador_rolagem < 2:
            indice = int(input( "Digite o índice do dado a ser removido (0 a 4):"))
            funcao = remover_dado(rolados,guardados,indice)
            rolados = funcao[0]
            guardados = funcao[1]
            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')
            contador_rolagem += 1
        
        if contador_rolagem == 2:
            print( "Você já usou todas as rerrolagens.")
        
        elif decisao == 3:
            l = len(rolados)
            rolados = rolar_dados(l)
            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')
        
        elif decisao == 4:
            imprime_cartela(cartela)
            print(f'Dados rolados: {rolados}')
            print(f'Dados guardados: {guardados}')
        
        elif decisao not in [0,1,2,3,4]:
            print("Opção inválida. Tente novamente.")
        
    if decisao == 0:
        categoria = int(input( "Digite a combinação desejada:"))

        dados = []
        for num in rolados:
            dados.append(num)
        for num in guardados:
            dados.append(num)

        verifica_categoria(categoria,cartela)

        faz_jogada(dados,categoria, cartela)
