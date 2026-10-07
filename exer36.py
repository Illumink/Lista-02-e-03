print("LANCHONETE BURGÃO")
print("PRODUTO             CÓDIGO         VALOR")
print("CACHORRO QUENTE      100         R$11,20")
print("OVO SIMPLES          101          R$8,30")
print("BAURU COM OVO        102         R$11,50")
print("HAMBURGUER           103         R$16,20")
print("REFRIGERANTE         201          R$6,00")
print("SUCO                 202          R$7,50")
print("ÁGUA MINERAL         203          R$4,70")

lanche = int(input("Digite o Código do Lanche: "))
bebida = int(input("Digite o Código da Bebida: "))

match lanche:
    case 100:
        valor_lanche = 11.2
        print("O Lanche escolhido foi Cachorro Quente.")
    case 101:
            valor_lanche = 8.3
            print("O Lanche escolhido foi Ovo Simples.")
    case 102:
            valor_lanche = 11.5
            print("O Lanche escolhido foi Bauru com Ovo.")
    case 103:
            valor_lanche = 16.2
            print("O Lanche escolhido foi Hamburguer.")

match bebida:
        case 201:
            valor_bebida = 6.0
            print("A Bebida escolhido foi Refrigerante.")
        case 202:
            valor_bebida = 7.5
            print("A Bebida escolhido foi Suco.")
        case 203:
            valor_bebida = 4.7
            print("A Bebida escolhido foi Agua Mineral.")

total = valor_bebida + valor_lanche

print(f"Valor Total a pagar R${total}")
