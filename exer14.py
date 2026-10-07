numero_da_conta = int(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o debito: "))
credito = float(input("Digite o credito: "))

saldo_atual = saldo - debito + credito
print(f"Saldo atual: {saldo_atual}")

if saldo_atual >=0:
    print(f"O saldo é positivo!")
else:
    print(f"O saldo é negativo!")