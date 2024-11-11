#Programa para saber os ganhos
def Salario():
    salario_hora = float(input("Quanto você ganha por hora: R$ "))
    horas_trabalhadas = float(input("Quantas horas você trabalha por mês: "))
    salario_bruto = salario_hora*horas_trabalhadas
    imposto_renda = salario_bruto*0.11
    inss = salario_bruto*0.08
    sindicato = salario_bruto*0.05
    salario_liquido = salario_bruto - inss - sindicato - imposto_renda
    print("Esta é a tabela do seu salário com os descontos: ")
    print(f"+ Salário bruto: R$ {salario_bruto:.2f}")
    print(f"- INSS (8%): R$ {inss:.2f}")
    print(f"- Sindicato (5%): R$ {sindicato:.2f}")
    print(f"- Imposto de Renda (11%): R$ {imposto_renda:.2f}")
    print(f"= Salário líquido: R$ {salario_liquido:.2f}")


Salario()