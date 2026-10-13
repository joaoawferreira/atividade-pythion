idade = int(input("Digite a idade: "))
estudante = input("Você é estudante? (s/n): ").lower()

if idade < 6:
    tipo = "gratuito"
    print("gratuito - R$ 0,00")
elif idade < 18 or idade >= 60 or estudante == "s":
    tipo = "meia-entrada"
    pagamento = input("Digite a forma de pagamento: (pix, credito, debito): ").lower()
    if pagamento == "pix":
            valor = 20 - (20 * 0.05)
    elif pagamento == "credito":
        valor = 20 + (20 * 0.05)
    elif pagamento == "debito":
        valor = 20
    print("meia-entrada - R$ ", valor)
else:
    tipo = "inteira"
    pagamento = input("Digite a forma de pagamento: (pix, credito, debito): ").lower()
    if pagamento == "pix":
        valor = 40 - (40 * 0.05)
    elif pagamento == "credito":
        valor = 40 + (40 * 0.05)
    elif pagamento == "debito":
        valor = 40
    print("inteira - R$ ", valor)
