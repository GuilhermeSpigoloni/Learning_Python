# 5.14
# 
soma = 0
media = 0
contadorMedia = 0
lista = []
while True:
    contadorMedia += 1
    numeros = int(input("Números Int(0 sair):  "))
    if numeros == 0:
        break
    soma += numeros
    lista.append(numeros)
# 
print(f"Quantidade de números inseridos: {contadorMedia - 1}")
print(f"Números inseridos: {lista}")
print(f"Soma: {soma}")
print(f"Média Aritmética: {soma/(contadorMedia - 1)}")
# 
# 
# 5.15
valorTotal = 0
print("--------Tabela--------\n-Produto -Código -Valor\n-Maça        1   R$0,50\n-Pera        2   R$1,00\n-Uva         3   R$4,00\n-Laranja     5   R$7,00\n-Melao       9   R$8,00")
while True:
    codigo = int(input("Código dos produtos(0 para finalizar a compra): "))
    if codigo == 0:
        break
    if codigo == 1:
        produto1 = 0.50
        valorTotal += produto1
    if codigo == 2:
        produto2 = 1
        valorTotal += produto2
    if codigo == 3:
        produto3 = 4
        valorTotal += produto3
    if codigo == 5:
        produto4 = 7
        valorTotal += produto4
    if codigo == 9:
        produto5 = 8
        valorTotal += produto5
    if codigo != 1 and codigo !=2 and codigo !=3 and codigo !=5 and codigo !=9:
        print("Código inválido!")
        break
        
print(f'Valor total a ser pago: R${valorTotal:.2f}')