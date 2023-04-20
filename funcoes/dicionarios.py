"""
Definições básicas sobre dicionários
"""

# dicionários
# tipo de dado que tem duas informações: chave, valor
# JSON
cliente = {
    "nome": "João",
    "endereco": "Av Brasil",
    "cep": "99010-000",
    "bairro": "Centro",
}
# print(cliente["nome"])
# print(cliente["endereco"])
# print(cliente.keys())
# print(cliente.values())

for chave, valor in cliente.items():
    print(f"{chave.upper()}: {valor}")
