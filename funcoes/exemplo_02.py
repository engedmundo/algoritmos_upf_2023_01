# FUAQ lê valores para um vetor V com 6 elementos.
# Após completar a leitura de todo o vetor,
# atualizar os elementos de índice ímpar com os
# valores dos seus próprios índices.
# No final, mostrar o vetor.

vetor = [0] * 6
# indices  0  1  2  3  4  5
qtd_elementos = len(vetor)

# for indice in range(6):
for indice in range(qtd_elementos):
    vetor[indice] = int(
        input(f"Informe o valor do elemento no indice {indice}: ")
    )

for indice, valor in enumerate(vetor):
    par = indice % 2

    if par != 0:
        vetor[indice] = indice

print(vetor)
