salario = float(input("Digite seu salario:R$ "))
aumento = float(input("Aumento:R$ "))
novo_salario = salario + (salario * aumento/100)
print(f"Seu novo salario sera: R${novo_salario:.2f}")