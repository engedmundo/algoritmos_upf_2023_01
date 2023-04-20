"""
Construa um algoritmo que faça a validação de CPF.
O programa deve receber o valor (números ou caracteres com máscara)
e retornar se o valor digitado é um cpf válido.

A validação do primeiro dígito consiste em efetuar a soma da multiplicação
dos 9 primeiros dígitos por uma sequência de 10 a 2.
Em seguida, deve-se obter o resto da divisão desta soma por 11.
Se o resto da divisão for igual ao primeiro dígito verificador, o dígito é
válido.
A validação do segundo dígito consiste em efetuar a soma da multiplicação dos
9 primeiros dígitos mais o primeiro dígito verificador por uma sequencia
de 11 a 2. Em seguida, deve-se obter o resto da divisão desta soma por 11.
Se o resto da divisão for igual ao segundo dígito verificador,
o dígito é válido.

Veja a referência:
https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/funcoes.js
"""


def ler_cpf():
    print("Digite o CPF que se deseja validar (digite somente números): ")
    repetir = True
    while repetir == True:
        cpf = input("cpf: ").replace(".", "").replace("-", "")

        if len(cpf) == 11:
            repetir = False
            return cpf
        else:
            print("A entrada deve conter 11 dígitos")


def validar_digito(cpf, digito):
    if digito == 1:
        tamanho_lista = 9
    else:
        tamanho_lista = 10

    # 9 primeiros dígitos
    digitos = cpf[0:tamanho_lista]
    # sequencia = [10, 9, 8, 7, ...]
    maior_sequencia = tamanho_lista + 1
    sequencia = list(range(maior_sequencia, 1, -1))
    soma = 0

    for indice, digito in enumerate(digitos):
        multiplicacao = sequencia[indice] * int(digitos[indice])
        soma = soma + multiplicacao

    # o simbolo % efetua a operação de resto da divisão
    resto = (soma * 10) % 11

    if resto == int(cpf[tamanho_lista]):
        return True
    else:
        return False


####################
# daqui pra frente é o nosso programa
cpf_entrada = ler_cpf()  # chamar e executar a função
# cpf_entrada = "22222222222"
primeiro_digito = validar_digito(cpf_entrada, 1)
segundo_digito = validar_digito(cpf_entrada, 2)

if primeiro_digito == True and segundo_digito == True:
    print(
        f"O CPF {cpf_entrada[0:3]}.{cpf_entrada[3:6]}.{cpf_entrada[6:9]}-{cpf_entrada[9:]} é válido."
    )
else:
    print(f"O CPF {cpf_entrada} é inválido.")
