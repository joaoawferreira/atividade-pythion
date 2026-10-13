l1 = float(input("Digite o comprimento do lado 1 do triângulo: "))
l2 = float(input("Digite o comprimento do lado 2 do triângulo: "))
l3 = float(input("Digite o comprimento do lado 3 do triângulo: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("Os lados formam um triângulo.")
    if l1 == l2 and l2 == l3:
        print("O triângulo é equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os lados não formam um triângulo.")