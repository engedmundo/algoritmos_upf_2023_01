# Faça um programa para jogar o jogo Pedra, papel e tesoura.
import random

alternativas_jogo = ["Pedra", "Papel", "Tesoura"]
encerrar_jogo = False
jogador = input("Informe o nome do jogador: ").capitalize()
placar_jogador = 0
placar_computador = 0
placar_empate = 0

while not encerrar_jogo:
    indice_escolha_computador = random.randint(0, 2)
    escolha_computador = alternativas_jogo[indice_escolha_computador]

    print(f"Alternativas possíveis: {alternativas_jogo}")
    escolha_jogador = input("Informe a alternativa: ").capitalize()

    if escolha_computador == "Pedra" and escolha_jogador == "Pedra":
        print("\nEmpate!!!")
        placar_empate += 1

    elif escolha_computador == "Pedra" and escolha_jogador == "Papel":
        print(f"\n{jogador} ganhou!!!")
        placar_jogador += 1

    elif escolha_computador == "Pedra" and escolha_jogador == "Tesoura":
        print("\nComputador ganhou!!!")
        placar_computador += 1

    elif escolha_computador == "Papel" and escolha_jogador == "Pedra":
        print("\nComputador ganhou!!!!")
        placar_computador += 1

    elif escolha_computador == "Papel" and escolha_jogador == "Papel":
        print("\nEmpate!!!!")
        placar_empate += 1

    elif escolha_computador == "Papel" and escolha_jogador == "Tesoura":
        print(f"\n{jogador} ganhou!!!")
        placar_jogador += 1

    elif escolha_computador == "Tesoura" and escolha_jogador == "Pedra":
        print(f"\n{jogador} ganhou!!!")
        placar_jogador += 1

    elif escolha_computador == "Tesoura" and escolha_jogador == "Papel":
        print("\nComputador ganhou!!!!")
        placar_computador += 1

    elif escolha_computador == "Tesoura" and escolha_jogador == "Tesoura":
        print("\nEmpate!!!!")
        placar_empate += 1
    else:
        print("\nEscolha inválida.")

    continuar_jogo = input(
        "Deseja jogar novamente? (s) para sim ou (n) para não: "
    )

    if continuar_jogo == "n":
        encerrar_jogo = True

print("\n------ PLACAR FINAL DO JOGO ------------")
print(f"{jogador}: {placar_jogador}")
print(f"Empate: {placar_empate}")
print(f"Computador: {placar_computador}")
