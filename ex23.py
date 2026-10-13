codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

if codigo == 1:
    preco = 4.50
elif codigo == 2:
    preco = 6.00
elif codigo == 3:
    preco = 7.00
elif codigo == 4:
    preco = 5.00
elif codigo == 5:
    preco = 3.00
else:
    print("Código de produto inválido")
    preco = 0

total = quantidade * preco
print("Total a pagar: R$ ", total)