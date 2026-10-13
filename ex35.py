num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)
elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero não é permitida.")
    else:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
else:
    print("Operador inválido.")