## 1- Soma de dois números:

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
soma = n1 + n2
print(f"A soma dos número é: {soma}")

## 2- Subtração de dois números:

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
subtracao = n1 - n2
print(f"A soma dos número é: {subtracao}")

# 3- Multiplicação de dois números:

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
multiplicacao = n1 * n2
print(f"A soma dos número é: {multiplicacao}")

# 4- Divisão de dois números:

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
divisao = n1 / n2
print(f"A soma dos número é: {divisao}")

# 5- Resto da divisão:

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
resto = n1 % n2
print(f"O resto da sua divisão é: {resto}")

# 6- Potência de um número:

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira a expoente: "))
potencia = n1 ** n2
print(f"A soma dos número é: {potencia}")

# 7- Média de três números:

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))
media = (n1 + n2 + n3) / 3
print(f"A soma dos número é: {media}")

# 8- Conversão de temperatura:

celsius = int(input("Insira a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} graus Celsius = {fahrenheit:.0f} Fahrenheit") 

# 9- Conversão de moeda:

moeda_real = float(input("Insira o valor em real: R$"))
dolar = moeda_real * 5.46
print(f"R${moeda_real} em dólares é ${dolar:.2f}")


# 10- Área de um retângulo: 

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
area = base * altura
print(f"A área do retangulo é: {area:.2f}")

# 11- Perímetro de um quadrado:

lado = float(input("Informe o valor do lado do quadrado: "))
perimetro = lado * 4 
print(f"O perímetro desse quadrado é: {perimetro:.2f}")

# 12- Área de um triângulo:

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
area = base * altura / 2
print(f"O valor da área desse triângulo é {area}")

# 13- Área de um círculo:

raio = float(input("Digite o valor do raio: "))
print("Ultilazando o valor π = 3.14159")
area = raio**2 * 3.14159
print(f"O valor da área desse círculo é aproximadamente: {area:.2f}")

# 14- Conversão de metros para centímetros:

metros = float(input("Digite o valor dos metros: "))
centimetros = metros * 100
print(f"{metros} m é = {centimetros}cm")

# 15- Cálculo de horas trabalhadas:

horas_trabalhadas = float(input("Horas trabalhadas: "))
valor_hora = float(input("Valor ganho por hora: R$"))
salario = horas_trabalhadas * valor_hora
print(f"O salário é: R${salario:.2f}")

# 16- Preço com desconto:

valor_produto = float(input("Digite o valor do produto: R$"))
desconto = float(input("Valor do desconto: "))
preco_final = valor_produto * (desconto/100)
print(f"O valor do produtor agora é: R${preco_final}")

# 17-  Calcular a velocidade média:

distancia_percorrida = float(input("Digite a distância percorrida: "))
tempo_gasto = float(input("Digite o tempo gasto nesse percurso: "))
velocidade_media = distancia_percorrida / tempo_gasto
print(f"A velocidade média durante o percurso foi de: {velocidade_media}")

# 18-  Converter idade em dias:

idade = int(input("Digite sua idade em anos: "))
idade_dias = idade * 365
print(f"{idade:.0f} em anos é: {idade_dias:.0f} dias")

# 19- Quantidade de segundos em um dia:

print("Quantos segundos tem em um dia? ")
dia = 24
segundos_dia = 24 * 60 * 60
print(f"Um dia possui {segundos_dia} segundos")

# 20- Calcular o IMC (Índice de Massa Corporal):

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura em metros: "))
imc= peso / (altura**2)
print(f"Seu IMC é: {imc}")

# 21- Diferença entre dois números:

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if (n1 <= 0 or n2 <= 0):
    print("Digite um valor positivo!")
else:
    diferenca = n1 // n2
    print(f"A diferença absoluta entre esse números é: {diferenca}")

# 22- Divisão inteira de dois números:

n1 = int(input("Digite o primeiro número (inteiro): "))
n2 = int(input("Digite o segundo número (inteiro): "))
divisao = n1//n2
print(f"Resultado {divisao}")

# 23- Valor absoluto de um número:

numero = float(input("Digite o algarismo que deseja saber o valor absoluto: "))
print(f"O valor absoluto é {numero}")

# 24- Converter km/h para m/s:

velocidade_km = float(input("Insira a velocidade em km/h: "))
velocidade_m = velocidade_km * 1000
print(f"{velocidade_km} km/h = {velocidade_m} m/s")

# 25- Fórmula de Bhaskara:

coeficiente_a = float(input("Digite o valor do coeficiente a: "))
coeficiente_b = float(input("Digite o valor do coeficiente b: "))
coeficiente_c = float(input("Digite o valor do coeficiente c: "))

delta = (coeficiente_b**2) - 4 * coeficiente_a * coeficiente_c

if delta < 0:
    print("Não existe raiz de número negativo!")
else:
    raiz = delta ** 0.5

    b = coeficiente_b * (-1)

    formula1 = (b + raiz) / (2 * coeficiente_a)
    formula2 = (b - raiz) / (2 * coeficiente_a)
    print(f"As raízes dessa equação são: \n X'= {formula1}\n X''= {formula2}")


# 26- Valor total de uma compra: 

produto1 = float(input("Digite o valor do primeiro produto: R$"))
produto2 = float(input("Digite o valor do segundo produto: R$"))
produto3 = float(input("Digite o valor do terceiro produto: R$"))
total = produto1 + produto2 + produto3
print(f"O valor total da compra deu R${total}")

# 27- Converter dias para semanas e dias:

dia = int(input("Insira os dias: "))
semana = dia // 7
resto = dia % 7
print(f"{dia} dia(s) = {semana} semana(s) e {resto} dia(s)")

# 28- Desconto progressivo:

produto = float(input("Insira o valor do produto: R$"))
if produto >= 100 and produto < 500:
    desconto = produto * 0.05
    produto_final = produto - desconto
    print(f"O valor do seu produto com o desconto é: R${produto_final:.2f}")
elif produto >= 500:
    desconto = produto * 0.10
    produto_final = produto - desconto
    print(f"O valor do seu produto com o desconto é: R${produto_final:.2f}")
else:
    print("Não há desconto sobre o valor deste produto")


# 29- Divisão com casas decimais limitadas:

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resultado = n1 / n2
print(f"O resultado dessa divisão é aproximadamente: {resultado:.2f} ")
