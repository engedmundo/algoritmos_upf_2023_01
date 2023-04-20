import math
import random


# aqui vamos declarar as funções para reutilização
def limpa_tela():
    # imprimir 100 linhas em branco
    for repeticao in range(100):
        print()


def matriz_inicial():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def instrucoes_iniciais():
    cabecalho = """
    #-------------------------------
            Instruções Iniciais
    #-------------------------------
    """
    instrucoes = """
    --- COMO JOGAR ---
    Digite um número correspondente à posição
    no tabuleiro para fazer sua jogada nela.
    Por exemplo, se você quer jogar no
    centro, digite 5

        1 | 2 | 3
          |   |  
       ---|---|---  
        4 | 5 | 6
          |   |  
       ---|---|---  
        7 | 8 | 9
          |   |  
       ---|---|---  

    Lembrando que seu símbolo será o X (xis)
    """
    print(cabecalho)
    print(instrucoes)


def verifica_jogador(valor):
    # (O)computador será igual -1
    # (X)jogador será igual 1
    # ( )espaço vazio igual a zero
    if valor == -1:
        return "O"
    elif valor == 1:
        return "X"
    else:
        return " "


def exibe_resultado_parcial(matriz):
    for linha in matriz:
        linha_para_mostrar = list()
        for valor in linha:
            valor_para_mostrar = verifica_jogador(valor)
            # adicionar valor ao final da lista
            linha_para_mostrar.append(valor_para_mostrar)
        print(
            f"{linha_para_mostrar[0]} | {linha_para_mostrar[1]} | {linha_para_mostrar[2]}"
        )


def entrada_do_jogador(matriz):
    valor_valido = False
    while valor_valido == False:
        jogada = input("Informe a sua jogada: ")
        # tentar executar uma ação
        try:
            jogada = int(jogada)

            if jogada >= 1 and jogada <= 9:
                indice_linha, indice_coluna = obter_indices_matriz(jogada)
                if matriz[indice_linha][indice_coluna] == 0:
                    valor_valido = True
                    return jogada
                else:
                    print(f"\n Joque em uma casa vazia. \n")
            else:
                print(f"\n O valor deve estar entre 1 e 9. \n")
        except:
            print(f"\n Somente números são permitidos. \n")


def obter_indices_matriz(jogada):
    jogada_transformada = jogada - 1
    indice_linha = math.floor(jogada_transformada / 3)
    indice_coluna = jogada_transformada % 3  # retorna o resto da divisão
    return indice_linha, indice_coluna


def atualiza_matriz_da_rodada(matriz, jogada, jogador):
    if jogador == "computador":
        simbolo_jogador = -1
    else:
        simbolo_jogador = 1

    indice_linha, indice_coluna = obter_indices_matriz(jogada)
    matriz[indice_linha][indice_coluna] = simbolo_jogador
    return matriz


def maquina_joga(matriz):
    repetir = True
    while repetir == True:
        jogada_do_computador = random.randint(1, 9)
        indice_linha, indice_coluna = obter_indices_matriz(jogada_do_computador)
        if matriz[indice_linha][indice_coluna] == 0:
            repetir = False
    return jogada_do_computador


def verifica_linha(linha):
    # [1, 1, 1] ou [-1, -1, -1]
    # [X, X, X] ou [O,   O,  O]
    soma = sum(linha)
    if soma == 3 or soma == -3:
        return True, soma
    else:
        return False, soma


def transpor_matriz(matriz):
    matriz_transposta = list()
    for indice_linha, linha in enumerate(matriz):
        nova_linha = list()
        for indice_coluna, _ in enumerate(linha):
            valor = matriz[indice_coluna][indice_linha]
            nova_linha.append(valor)
        matriz_transposta.append(nova_linha)
    return matriz_transposta


def obter_diagonais(matriz):
    diagonal_principal = [matriz[0][0], matriz[1][1], matriz[2][2]]
    diagonal_secundaria = [matriz[0][2], matriz[1][1], matriz[2][0]]
    diagonais = [diagonal_principal, diagonal_secundaria]
    return diagonais


def verifica_vencedor(matriz):
    # verificação das linhas
    for linha in matriz:
        tem_vencedor, soma = verifica_linha(linha)
        if tem_vencedor == True:
            return True, soma

    # verificação das colunas
    matriz_transposta = transpor_matriz(matriz)
    for coluna in matriz_transposta:
        tem_vencedor, soma = verifica_linha(coluna)
        if tem_vencedor == True:
            return True, soma

    # verificar diagonais
    diagonais = obter_diagonais(matriz)
    for diagonal in diagonais:
        tem_vencedor, soma = verifica_linha(diagonal)
        if tem_vencedor == True:
            return True, soma

    return False, 0


######## aqui inicia o nosso programa
limpa_tela()
instrucoes_iniciais()
matriz_da_rodada = matriz_inicial()
disputas_restantes = 4
tem_vencedor = False

while disputas_restantes > 0 and tem_vencedor == False:
    jogada_do_jogador = entrada_do_jogador(matriz_da_rodada)
    matriz_da_rodada = atualiza_matriz_da_rodada(
        matriz_da_rodada, jogada_do_jogador, "jogador"
    )
    jogada_do_computador = maquina_joga(matriz_da_rodada)
    matriz_da_rodada = atualiza_matriz_da_rodada(
        matriz_da_rodada, jogada_do_computador, "computador"
    )
    exibe_resultado_parcial(matriz=matriz_da_rodada)
    tem_vencedor, soma = verifica_vencedor(matriz_da_rodada)

    if tem_vencedor == True:
        # operação ternária
        # vecedor recebe jogador se a soma é igual a 3, senão recebe computador
        vencedor = "Jogador" if soma == 3 else "Computador"
        print(f"\n VENCEDOR: {vencedor}!! \n")

    disputas_restantes -= 1  # diminuindo 1 valor da contagem
