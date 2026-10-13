jog1 = input("Digite a escolha da jogada do jogador 1 (pedra, papel ou tesoura): ")
jog2 = input("Digite a escolha da jogada do jogador 2 (pedra, papel ou tesoura): ")

if jog1 == jog2:
    print("Empate!")
elif (jog1 == "pedra" and jog2 == "tesoura") or (jog1 == "papel" and jog2 == "pedra") or (jog1 == "tesoura" and jog2 == "papel"):
    print("Jogador 1 venceu!")
elif (jog2 == "pedra" and jog1 == "tesoura") or (jog2 == "papel" and jog1 == "pedra") or (jog2 == "tesoura" and jog1 == "papel"):
    print("Jogador 2 venceu!")
else:
    print("Jogada inválida.")