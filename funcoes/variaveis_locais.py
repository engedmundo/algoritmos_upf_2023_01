"""
Exemplo para explicação de uma variável local e global
"""

variavel = "Eu sou uma variável global"


def diga_ola():
    print("Olá")
    variavel = "A variável global foi alterada dentro da função"
    variavel_local = "Eu sou uma variável local"
    # dentro da funçao temos acesso a variaveis globais
    print(variavel)
    print(variavel_local)
    return


def diga_bom_dia():
    variavel_local = "Eu sou outra variavel local de outra função"
    print(variavel_local)
    return


diga_ola()
print(variavel)
diga_bom_dia()
