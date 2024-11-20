depositoInicial = float(input("Deposito inicial: "))
taxa = float(input("Taxa de juros(%/mes): "))
taxaUso = taxa/100
renda = depositoInicial
tempo = int(input("Tempo em meses: "))

x = 0
while x < tempo:
    x += 1
    composto = (renda * taxa/100)
    renda += composto

    
    print(f'Mês {x}: R${renda:.2f}')


montante = renda
print(f'Montante final: R${montante:.2f}')

