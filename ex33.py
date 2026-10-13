idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você não pode votar.")
elif idade <= 17:
    print("Voto facultativo.")
elif idade <= 70:
    print("Voto obrigatório.")
else:
    print("Voto facultativo.")