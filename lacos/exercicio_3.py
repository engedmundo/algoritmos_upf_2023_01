"""
Faça um algoritmo que lê valores para uma variável Y.
Os valores devem ser inseridos em uma lista.
Em seguida, verificar quais são os valores pares. 
Retornar os valores pares, a soma de todos os valores pares e a média dos 
valores pares
"""

variavel_y = 1
valores_digitados = []

while variavel_y != 0:
    variavel_y = int(input("Informe o valor de y: "))
    # adicionar y para dentro da lista
    valores_digitados.append(variavel_y)

valores_pares = []
soma_pares = 0

for valor in valores_digitados:
    resto = valor % 2
    if resto == 0:
        valores_pares.append(valor)
        soma_pares += valor

media = soma_pares / (len(valores_pares) - 1)

print(f"Valores pares: {valores_pares}")
print(f"Soma dos pares: {soma_pares}")
print(f"Média dos pares: {media}")
