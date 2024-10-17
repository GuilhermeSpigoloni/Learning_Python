
## LISTA 02 - PRÁTICA

print("----------Exercício a ser executado----------")
print("1 - Número Positivo ou negativo")
print("2 - Maioridade")
print("3 - Par ou ímpar")
print("4 - Número maior")
print("5 - Desconto de compra")
print("6 - Verificar múltiplo")
print("7 - Cálculo de média")
print("8 - Senha correta")
print("9 - Entrada gratuita")
print("10 - Verificar nota")
print("11 - Categoria de idade")
print("12 - Maior de três números")
print("13 - Divisão segura")
print("14 - Número dentro de intervalo")
print("15 - Aprovado, recuperação ou reprovado")
print("16 - Calcular IMC")
print("17 - Indentificar Triângulo")
print("18 - Login e senha")
print("19 - Verificar maioridade para dirigir")
print("20 - Sair")
escolha = input("Escolha um exercício: ")



if escolha == '1':
# 01
    numero = float(input("Insira um número: "))
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é 0.")

elif escolha == '2':
# 02
    print("-----MAIORIDADE-----")
    idade = int(input("Informe sua idade: "))

    if idade < 18:
        print("Você é menor de idade.")
    else:
        print("Você já alcançou a maioridade.")

elif escolha == '3':
# 03
    numero = float(input("Digite um valor: "))
    if numero % 2 != 0:
        print("O número é impar.")
    else:
        print("O número é par.")

elif escolha == '4':
# 04 
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    if n1 > n2:
        print(f"O maior número é {n1}")
    elif n2 > n1:
        print(f"o maior número é {n2}")
    else:
        print("Fica suave.")

elif escolha == '5':
# 05
    valor_compra = float(input("Insira o valor da compra: R$"))
    if valor_compra > 100:
        valor_compra = valor_compra - (valor_compra * 10/100)
        print(f"O valor da compra com desconto é R${valor_compra:.2f}")
    else:
        print(f"Não houve desconto\nValor a pagar: R${valor_compra:.2f}")

elif escolha == '6':
# 06
    numero = float(input("Insira um valor: "))
    if numero % 5 == 0:
        print("O número é múltiplo de 5.")
    else:
        print("O número não é múltiplo de 5.")

elif escolha == '7':
# 07
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3

    if media >= 7:
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado!")

elif escolha == '8':
# 08
    senha = input("Senha: ")
    senha_correta = 'python_123_EFG'

    if senha == senha_correta:
        print("Acesso permitido.")
    else:
        print("Senha incorreta.")

elif escolha == '9':
# 09
    idade = int(input("Insira sua idade: "))
    if idade <= 5 or idade >= 60:
        print("Possui direito à entrada gratuita.")
    else:
        print("Somente pagando pra entrar paizão.")

elif escolha == '10':
# 10
    nota = float(input("Insira uma nota de 0 a 10: "))
    if nota < 0 or nota >= 11:
        print("ERRO: INSIRA UM VALOR VÁLIDO!")
    else:
        print(f"Nota: {nota}/10")

elif escolha == '11':
# 11
    idade = int(input("Insira sua idade:"))
    if idade < 12:
        print("Criança")
    elif idade >= 12 and idade <= 17:
        print("Adolescente")
    else:
        print("Adulto")
    
elif escolha == '12':
# 12
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Terceiro número: "))

    if n1 > n2 and n1 > n3:
        print(f"Maior número: {n1}")
    elif n2 > n1 and n2 > n3:
        print(f"Maior número: {n2}")
    else:
        print(f"Maior número: {n3}")

elif escolha == '13':
# 13
    n1 = float(input("Insira o valor do dividendo:"))
    n2 = float(input("Insira o valor do divisor:"))
    quociente = n1 / n2
    if n2 == 0:
        print("Não existe divisão por 0!")
    else:
        print(f"Resultado: {quociente}")
        
elif escolha == '14':
# 14
    numero = float(int("Insira um valor: "))
    if numero >= 10 and numero <=50:
        print("O número está entre 10 e 50.")
    else:
        print("O número não está entre 10 e 50.")

elif escolha == '15':
# 15
    n1 = float(input("Insira a primeira nota: "))
    n2 = float(input("Insira a segunda nota: "))
    n3 = float(input("Insira a terceira nota: "))
    media = (n1 + n2 + n3) / 3

    if media >= 7:
        print("Aprovado")
    elif media < 7 and media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

elif escolha == '16':
# 16
    peso = float(input("Peso(kg): "))
    altura = float(input("Altura(m): "))
    imc = peso / (altura**2)

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc >= 18.5 and imc < 25:
        print("Seu peso está normal")
    else:
        print("Você está acima do peso")
    
elif escolha == '17':
# 17
    lado1 = float(input("Digite o valor do primeiro lado: "))
    lado2 = float(input("Digite o valor do segundo lado: "))
    lado3 = float(input("Digite o valor do terceiro lado: "))

    if (lado1 + lado2) > lado3 or (lado1 + lado3) > lado2 or (lado2 + lado3) > lado1:
        if lado1 == lado2 and lado1 == lado3:
            print("Triângulo Equilátero.")
        elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1 or lado1 == lado3 and lado1 != lado2:
            print("Triângulo Isósceles.")
        elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
            print("Triângulo Escaleno.")
        else:
            print("Não consigo identificar qual tipo de triângulo seria esse.")
    else:
        print("Essa figura não se enquadra como um triângulo!")

elif escolha == '18':
# 18
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == 'admin' and senha == '1234':
        print("Login Bem sucedido.")
    else:
        print("Usuário ou/e senha incorreto(s).")

elif escolha == '19':
# 19
    idade = int(input("Insira sua idade: "))
    if idade >= 18:
        print("Você já pode dirigir!")
    else:
        print(f"Faltam {18 - idade}ano(s) para você poder dirigir.")

elif escolha == '20':
    print("Até mais...")

else:
    print("Faça uma escolha válida!")






