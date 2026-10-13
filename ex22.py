temp = float(input("Digite a temperatura em Celsius: "))

if temp < 0:
    print("Abaixo de zero - risco de geada!")
elif temp <= 10:
    print("Muito frio - use agasalho!")
elif temp <= 18:
    print("frio")
elif temp <= 25:            
    print("Agradavel")
else: 
    print("Calor")