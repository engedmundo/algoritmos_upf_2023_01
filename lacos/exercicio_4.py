"""
Faça um programa que calcule as raízes de uma equação de 2 grau
"""

import math

valor_a = float(input("Insira o valor de 'A': "))
valor_b = float(input("Insira o valor de 'B': "))
valor_c = float(input("Insira o valor de 'C': "))

if valor_a == 0:
    print("Não é uma equação de 2 grau.")

else:
    delta = (valor_b**2) - (4 * valor_a * valor_c)
    print(f"Delta -> {delta}")

    if delta < 0:
        print("Não existem raízes reais")
    elif delta == 0:
        print("Raiz única")
        raiz_unica = (-1 * valor_b) / (2 * valor_a)
        print(f"Raiz: {raiz_unica}")
    else:
        print("A equação tem duas raízes")
        # primeira_raiz = (-1 * valor_b + delta ** (1/2)) / (2 * valor_a)
        primeira_raiz = (-1 * valor_b + math.sqrt(delta)) / (2 * valor_a)
        segunda_raiz = (-1 * valor_b - math.sqrt(delta)) / (2 * valor_a)
        print("Primeira raiz: {primeira_raiz:.2f}")
        print("Segunda raiz: {segunda_raiz:.2f}")
