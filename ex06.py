preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
pago = float(input("Digite o valor pago: "))
total = preco * quantidade
print("O total da compra é: R$ ",  total, "\n O troco é: R$ ", pago - total)