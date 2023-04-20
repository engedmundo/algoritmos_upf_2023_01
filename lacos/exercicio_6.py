numero = input("Digite um número: ")

if int(numero) <= 0:
    print("Número inválido")
else:
    soma = 0
    for digito in numero:
        soma = soma + int(digito)

    print(f"Soma -> {soma}")
