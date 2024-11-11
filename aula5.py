# categoria = int(input("Digite a caregoria do produto: "))
# if categoria == 1:
#     preco = 10
# else:
#     if categoria == 2:
#         preco = 18
#     else:
#         if categoria == 3:
#             preco = 23
#         else:
#                 if categoria == 4:
#                     preco: 26
#                 else:
#                      if categoria == 5:
#                         preco = 31
#                      else:
#                          print("Categoria inválida")
#                          preco = 0

# print(f"O preço do produto é: R${preco:.2f}")

# ###############################################################################

# categoria = int(input("Digite a caregoria do produto: "))
# if categoria == 1:
#     preco = 10
#     print(f"O preço do produto é: R${preco:.2f}")
# elif categoria == 2:
#     preco = 18
#     print(f"O preço do produto é: R${preco:.2f}")
# elif categoria == 3:
#     preco = 23
#     print(f"O preço do produto é: R${preco:.2f}")
# elif categoria == 4:
#     preco = 26
#     print(f"O preço do produto é: R${preco:.2f}")
# elif categoria == 5:
#     preco = 31
#     print(f"O preço do produto é: R${preco:.2f}")
# else: 
#     preco = 0
#     print("Categoria inválida")
#     print(f"O preço do produto é: R${preco:.2f}")


# ###############################################################################

# ATIVIDADE

# # 4.8
# n1 = float(input("Primeiro número: "))
# operacao = input("Operação (+,-,/,*)")
# n2 = float(input("Segundo número: "))

# if operacao == '+':
#     print(f"Resultado: {n1+n2}")
# elif operacao == '-':
#     print(f"Resultado: {n1-n2}")
# elif operacao == '/':
#     if n2 != 0:
#         print(f"Resultado: {n1/n2}")
#     else:
#          print("Divisão por 0 não existe!")
# elif operacao == '*':
#     print(f"Resultado: {n1*n2}")
# else:
#     print("Erro!")


# # 4.9
# print("-----Empréstimo Bancário-----")
# casa = float(input("Valor da casa: R$"))
# salario = float(input("Seu salário: R$"))
# anos = int(input("Quantidade de anos a pagar: "))

# prestacao = casa/(anos*12) 
# if prestacao <= (salario * 0.30):
#     print(f"Empréstimo aprovado!\nPrestações: R${prestacao:.2f}")
# else:
#     print(f"Empréstimo negado!\nPrestação: R${prestacao:.2f}\n-Salário incompatível com o valor das parcelas.\nTente parcelar em um tempo maior.")



# # 4.10
# print("-----Preço a pagar pelo fornecimento de energia-----")
# consumo = float(input("Consumo de Kwh: "))
# tipo = input("Instalações:\n-Residencial\n-Comercial\n-Industrial\nQual o seu tipo: ").lower()

# if tipo == 'residencial':
#     if consumo <= 500:
#         print(f"Preço a pagar R${consumo * 0.40:.2f}")
#     else:
#         print(f"Preço a pagar: R${consumo * 0.65:.2f}")
# elif tipo == 'comercial':
#         if consumo <= 1000:
#             print(f"Preço a pagar: R${consumo * 0.55:.2f}")
#         else:
#              print(f"Preço a pagar: R${consumo * 0.60:.2f}")        
# elif tipo == 'industrial':
#      if consumo <= 5000:
#           print(f"Preço a pagar: R${consumo * 0.55:.2f}")
#      else:
#           print(f"Preço a pagar: R${consumo * 0.60:.2f}")
# else:
#      print("Escolha uma opção válida")



# LAÇOS DE REPETIÇÃO
# ESTRUTURA DE REPETIÇÃO WHILE --> ENQUANTO
# WHILE <CONDIÇÃO>:
    #BLOCO A SER EXECUTADO
# x = 1
# while x <= 5:
#     print("Carbonos")
#     print(1)
#     print(x)
#     x = x + 1

# print("------------------------------------")
# print(x)

############################################################

# y = 1
# while y <= 3:
#     print(y)
#     y = y + 1

#############################################################


# # 5.1 
# x = 1
# while x <= 100:
#     print(f"Número: {x}")
#     x = x + 1

## 5.2
# y = 50
# while y <= 100:
#     print(f"Número: {y}")
#     y = y + 1

# 5.3
z = 10
while z >= 0:
    print(f"Decolar em: {z}")
    z = z - 1
print("----------------------------")
print(z)
