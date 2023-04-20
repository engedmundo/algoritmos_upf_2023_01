# FUAQ lê valores para um vetor W[6].
# Após, encontrar e mostrar o maior valor e a
# posição em que ele está no vetor.

vetor = [25, 12, 7, 59, 32, 18]
maior_valor = -1
indice_do_maior_valor = 0

for indice, valor in enumerate(vetor):
    if valor > maior_valor:
        maior_valor = valor
        indice_do_maior_valor = indice

print(f"O maior valor é {maior_valor}")
print(f"O indice do maior valor é {indice_do_maior_valor}")
