print("---------------Escolha oque desea fazer.---------------")
print("1 - Descobrir se já é de maior.")
print("2 - Descobrir se determinados números são iguais.")
print("3 - Descobrir se um número é positivo ou negativo.")
print("4 - Sair.")
escolha = input("Faça sua escolha: ")




# Exercício 01
if escolha == '1':
    print("-----MAIORIDADE-----")
    idade = int(input("Informe sua idade: "))

    if idade < 18:
        print("Você é menor de idade.")
    else:
        print("Você já alcançou a maioridade.")


# Exercício 02

elif escolha == '2':
    print("-----NÚMEROS IGUAIS-----")
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))

    if x == y:
        print("Os números são iguais!!!")
    else:
        print("Os números são diferentes.")


# Exercício 03

elif escolha == '3':
    print("-----POSITIVO/NEGATIVO-----")
    numero = float(input("Insira um número: "))
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é 0.")


elif escolha == '4':
    print("Saindo...")


else:
    print("Digite um número válido!")
