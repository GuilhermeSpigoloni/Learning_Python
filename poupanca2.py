depositoInicial = float(input("Deposito inicial: "))
taxa = float(input("Taxa de juros(%/mes): "))
taxaUso = taxa/100
renda = depositoInicial
tempo = int(input("Tempo em meses: "))
valorMes = 0
x = 0
while x < tempo:
    x += 1
    composto = (renda * taxa/100)
    renda += composto
    valorMes = float(input(f'Valor adicional a ser depositado no mês {x}: R$'))
    renda += valorMes
    
    print(f'Mês {x}: R${renda:.2f}')


montante = renda
print(f'Montante final: R${montante:.2f}')

