turno = input("Digite o turno que você estuda (M-Matutino, V-Vespertino, N-Noturno): ")

if turno == "M" or "m":
    print("Bom Dia!")
elif turno == "V" or "v":
    print("Boa Tarde!")
elif turno == "N" or "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
