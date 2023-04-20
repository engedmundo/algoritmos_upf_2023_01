# desenvolva um algoritmo de ordenação de vetores do tipo bubble sort

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def compara_valores(vetor, indice_inicio, indice_fim):
    if vetor[indice_inicio] > vetor[indice_fim]:
        return True
    else:
        return False


def troca_valores(vetor, indice_inicio, indice_fim):
    (
        vetor[indice_inicio],
        vetor[indice_fim],
    ) = (
        vetor[indice_fim],
        vetor[indice_inicio],
    )
    return vetor


def ordenar_linha():
    pass


qtd_elementos = len(lista)

for repeticao in range(qtd_elementos):
    for indice in range(qtd_elementos - 1):
        deve_trocar = compara_valores(lista, indice, indice + 1)
        if deve_trocar:
            lista = troca_valores(lista, indice, indice + 1)

print(lista)
