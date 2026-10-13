valor = float(input("Digite o valor da compra: "))

if valor < 50:
    desconto = valor * 0
elif valor < 100:
    desconto = valor * 0.05
elif valor < 200:
    desconto = valor *  0.10
else:
    desconto = valor * 0.15
print("Desconto aplicado: R$", desconto, "Valor final: R$", valor - desconto)