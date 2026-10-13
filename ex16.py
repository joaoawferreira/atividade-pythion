saldo = float(input("Digite o saldo da conta: "))
saque = float(input("Digite o valor do saque: "))
if saldo >= saque:
    print("Saque realizado com sucesso! Saldo atual: R$ ", saldo - saque)
else:
    print("Saldo insuficiente")