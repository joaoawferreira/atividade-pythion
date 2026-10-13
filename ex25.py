vel_car = float(input("Digite a velocidade do carro (km/h): "))
vel_via = float(input("Digite a velocidade da via (km/h): "))

percentual_excesso = (vel_car - vel_via) / vel_via * 100

if percentual_excesso <= 0:
    print("Velocidade dentro do limite permitido.")
elif percentual_excesso <= 20:
    print("Infração média")
elif percentual_excesso <= 50:
    print("Infração grave")
else:
    print("Infração gravíssima")