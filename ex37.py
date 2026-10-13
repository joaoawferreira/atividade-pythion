num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


if (num1 > num2 and num1 > num3) and num2 > num3:
    print("A sequencia crescente é:", num3, ",", num2, ",", num1)
elif (num1 > num2 and num1 > num3) and num3 > num2:
    print("A sequencia crescente é:", num2, ",", num3, ",", num1)
elif (num2 > num1 and num2 > num3) and num1 > num3:
    print("A sequencia crescente é:", num3, ",", num1, ",", num2)
elif (num2 > num1 and num2 > num3) and num3 > num1:
    print("A sequencia crescente é:", num1, ",", num3, ",", num2)
elif (num3 > num1 and num3 > num2) and num1 > num2:
    print("A sequencia crescente é:", num2, ",", num1, ",", num3)
else:
    print("A sequencia crescente é:", num1, ",", num2, ",", num3)