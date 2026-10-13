cA = float(input("Digite o coeficiente A: "))
cB = float(input("Digite o coeficiente B: "))
cC = float(input("Digite o coeficiente C: "))

if cA == 0:
    print("Não é uma equação do segundo grau.")
else:
    delta = cB*cB - 4 * cA * cC
    if delta < 0:
        print("não possui raízes reais.")
    elif delta == 0:
        raiz = -cB / (2 * cA)
        print(" uma raiz : x = ", raiz)
    else:
        raiz1 = (-cB + delta**0.5) / (2 * cA)
        raiz2 = (-cB - delta**0.5) / (2 * cA)
        print("X1 = ", raiz1, "e ", "X2 = ", raiz2)