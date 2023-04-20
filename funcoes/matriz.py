# função para retornar uma matriz transposta


def transpor_matriz(matriz):
    matriz_transposta = list()
    for indice_linha, linha in enumerate(matriz):
        nova_linha = list()
        for indice_coluna, _ in enumerate(linha):
            valor = matriz[indice_coluna][indice_linha]
            nova_linha.append(valor)
        matriz_transposta.append(nova_linha)
    return matriz_transposta


matriz_original = [
    [1, 0, -1],
    [0, 2, 1],
    [1, -3, -1],
]

matriz_transposta = transpor_matriz(matriz_original)
print(matriz_original)
print(matriz_transposta)
