#Número 3.7
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
print(f"A soma dos números é: {soma}")

#Número 3.8

metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"A quantidade de centimetros é: {milimetros}")

#Número 3.9

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print(f"O total de segundos é: {total}")

#Número 3.10

salario = float(input("Digite o valor do seu salário: "))
aumento = float(input("Digite o valor do aumento em porcentagem: "))
novo_salario = salario + (salario * (aumento / 100))
print(f"O seu novo salário é: {novo_salario}")

#Número 3.11

mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o valor do desconto em porcentagem: "))
valor_final = mercadoria - (mercadoria * (desconto / 100))
print(f"O valor final da mercadoria é: {valor_final}")

#Número 3.12

distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo que levou para percorrer essa distância: "))
velocidade = distancia / tempo
print(f"A velocidade média é: {velocidade}")

#Número 3.13

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")

#Número 3.14

km = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = int(input("Digite a quantidade de dias que ficou com o carro: "))
preco = (km * 0.15) + (dias * 60)

#Número 3.15

cigarros = float(input("Digite a quantidade de cigarros fumados por dia: "))
anos = float(input("Digite a quantidade de anos que fuma: "))
cigarros_total = cigarros * (anos * 365)  #cada ano tem 365 dias
dias_perdidos = cigarros_total * 10 / 60 / 24   #10 minutos de vida perdidos por cigarro, cada dia tem 24h e cada hora 60 minutos, por isso a divisão
print(f"Você perdeu {dias_perdidos:.0f} dias de vida")

