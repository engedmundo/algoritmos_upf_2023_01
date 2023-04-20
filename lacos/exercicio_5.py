salario = float(input("Informe o valor do salário atual, em R$: "))
tempo_servico = int(input("Informe o tempo de serviço, em anos: "))

if salario < 500:
    percentual_reajuste = 0.25
elif salario < 1000:
    percentual_reajuste = 0.20
elif salario < 1500:
    percentual_reajuste = 0.15
elif salario < 2000:
    percentual_reajuste = 0.10
else:
    percentual_reajuste = 0

reajuste = salario * percentual_reajuste

if tempo_servico <= 1:
    bonus = 0
elif tempo_servico <= 3:
    bonus = 100
elif tempo_servico <= 6:
    bonus = 200
elif tempo_servico <= 10:
    bonus = 300
else:
    bonus = 500

novo_salario = salario + reajuste + bonus

print(f"Reajuste: R$ {reajuste:.2f}")
print(f"Bonus: R$ {bonus:.2f}")
print(f"Novo salário é igual a R$ {novo_salario:.2f}")
