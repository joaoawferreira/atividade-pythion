saque = int(input("Digite o valor do saque: "))

if saque % 10 != 0 or saque == 0:
    print("Valor inválido para saque")
else:
    notas_100 = saque // 100
    saque %= 100
    if notas_100 != 0:
        print("Notas de R$100:", notas_100)
    notas_50 = saque // 50
    saque %= 50
    if notas_50 != 0:
        print("Notas de R$50:", notas_50)
    notas_20 = saque // 20
    saque %= 20
    if notas_20 != 0:
        print("Notas de R$20:", notas_20)
    notas_10 = saque // 10
    if notas_10 != 0:
        print("Notas de R$10:", notas_10)