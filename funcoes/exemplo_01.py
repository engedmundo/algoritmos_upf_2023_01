"""
FUAQ lê valor para uma variável M e um valor para a variável N.
Calcular o valor de M multiplicado por N numa função.
Mostrar o resultado no programa principal.

def -> palavra reservada, sempre tem que começar por def
nome_da_funcao -> segue a mesma regra de nomes de variáveis
parâmetros -> o que a função deve receber para funcionar
"""


def multiplica(m, n):
    resultado = m * n
    # o que a função irá devolver a quem o chamou
    return resultado


"""
variavel_m = int(input("Informe o valor de M: "))
variavel_n = int(input("Informe o valor de N: "))

resultado = multiplica(variavel_m, variavel_n)

print(f"Resultado da multiplicação: {resultado}")
"""


def saudacao(nome, idade):
    ano_atual = 2023
    data_nascimento = ano_atual - idade
    print(f"Olá {nome}!! Você nasceu em {data_nascimento}")
    return


nome = "João"
saudacao(idade=30, nome=nome)
saudacao(idade=20, nome="Maria")
