vel = int(input("Digite a velocidade: "))
if vel > 80:
    print("Você foi multado! você passou ", vel-80, " km/h do limite")
else:
    print("Você está dentro do limite de velocidade")