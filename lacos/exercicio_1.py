# FUAQ lê a idade de 2 filhos de 4 casais
# calcula e mostra a soma das idades dos 2 filhos da cada casal.
# Importante mostrar a ordem de leitura dos casais.


numero_casal = 1
# for numero_casal in range(1, 5, 1):
while numero_casal <= 4:
    print(f"Casal numero {numero_casal}: \n")

    primeiro_filho = int(input("Informe a idade do primeiro filho: "))
    segundo_filho = int(input("Informe a idade do segundo filho: "))

    soma_idades = primeiro_filho + segundo_filho

    print(f"\nA soma das idades é: {soma_idades}\n")
    numero_casal += 1
