# Atividade vídeo

# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h

velocidade = float(input("Velocidade do veículo (km/h): "))
if velocidade > 80:
    print("O motorista foi multado.")
    print(f"Limite: 80km/h\nSua velocidade: {velocidade}km/h") 
    multa = (velocidade - 80) * 5
    print(f"O valor da multa: R${multa:.2f}")

else: 
    print("Você não foi multado.")


# Exercício 4.3 - Escreva um programa que leia três números e que imprimo o maior e menor.


n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"Maior número {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior número é {n2}")
elif n3 > n2 and n3 > n1:
    print(f"Maior número {n3}")
else:
    print("Por Favor, coloque um número real!")

if n1 < n2 and n1 < n3:
    print(f"O menor número é {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor número é o {n2}")
elif n3 < n2 and n3 < n1:
    print(f"O menor número é o {n3}")
else: 
    print("Por Favor, coloque um número real!")

# Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os salários iguai ou inferiores, de 15%

funcionario = input("Nome: ")
salario = float(input("Salário: R$"))
if salario > 1250:
    aumento = salario + (salario * (10/100))
    print(funcionario)
    print(f"Salário antigo: R${salario:.2f}\nNovo salário: R${aumento:.2f}")
elif salario <= 1250:
    aumento = salario + (salario * (15/100))
    print(funcionario)
    print(f"Salário antigo: R${salario:.2f}\nNovo salário: R${aumento:.2f}")

else:
    print("Valor inválido!")

    

# Atividade postada grupo

# 3 - Uma loja de produtos eletrônicos com vendas regulares opta por contratar uma equipe para a organização de um sistema de gerenciamento de vendas. Seu desafio será elaborar um algoritmo que, a partir de dados fornecidos pelo usuário, 
# calcule o valor da venda de um produto, exibindo uma saída em vídeo contendo o código do produto, o nome, a quantidade comprada, o valor unitário e valor total.

nome_produto = input("Nome do produto: ")
codigo_produto = input("Código produto: ")
quantidade = int(input("Quantidade comprada: "))
valor_unitario = float(input("Valor unitário do produto: R$"))

valor_final = quantidade * valor_unitario

print("\n\n\n--- Resumo da Venda ---")
print(f"Código do Produto: {codigo_produto}")
print(f"Nome do Produto: {nome_produto}")
print(f"Quantidade Comprada: {quantidade}")
print(f"Valor Unitário: R$ {valor_unitario:.2f}")
print(f"Valor Total: R$ {valor_final:.2f}")





# 4 - Uma empresa concederá um reajuste salaria de 8,75% no próximo mês. Sua missão é elaborar um algoritmo que, a partir de dados inseridos pelo usuário, 
# calcule o salário reajustando, seu nome, o valor de seu salário atual e o valor do salário reajustado

nome = input("Insira seu nome: ")
salario_atual = float(input("Insira seu salário atual: R$"))
novo_salario = salario_atual * (8.75/100)
print(f"{nome}\nSalário antigo: R${salario_atual:.2f}\nNovo salário: R${novo_salario:.2f}")

# 5 - As lojas de um shopping center estão concedendo 10% de desconto no preço de qualquer produto. Faça um algoritmo que, a partir do valor fornecido, calcule e exiba o preço atual e o preço com o desconto.

produto = float(input("Valor do produto: R$"))
desconto = produto * (10/100)
print(f"Valor produto: R${produto:.2f}\nValor com desconto: R${desconto:.2f}")


