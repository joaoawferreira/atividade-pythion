n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência (em %): "))
media = (n1 + n2) / 2

if media >= 7 and frequencia >= 75:
    print("Aprovado")
elif media < 7 and frequencia >= 75:
    print("Reprovado por nota")
elif media >= 7 and frequencia < 75:
    print("Reprovado por faltas")
else:
    print("Reprovado por nota e faltas")