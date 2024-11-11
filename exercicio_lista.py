# ATIVIDADE 22/10/2024

#11 
#a)
# n1 = float(input("Primeiro número: "))
# n2 = float(input("Segundo número: "))
# n3 = float(input("Terceiro número: "))
# n4 = float(input("Quarto número: "))

# if n1 > n2 and n1 > n3 and n1 > n4:
#     print(f"Maior número: {n1}")
# elif n2 > n1 and n2 > n3 and n2 > n4:
#     print(f"Maior número: {n2}")
# elif n3 > n2 and n3 > n1 and n3 > n4:
#     print(f"Maior número: {n3}")
# elif n4 > n2 and n4 > n1 and n4 > n1:
#     print(f"Maior número: {n4}")
# else:
#     print("Erro!")

#b)
# n1 = int(input("Primeiro número: "))
# n2 = int(input("Segundo número: "))
# n3 = int(input("Terceiro número: "))
# lista=[n1,n2,n3]
# print(sorted(lista))

#c)
# print("-------Verifique se o número é ímpar e se ele é multiplo de outro número--------")
# n = float(input("Número: "))
# mult = int(input("Múltiplo de: "))

# if n % 2 != 0:
#     print("O número é ímpar!")
# else:
#     print("O número é par!")

# if n % mult == 0:
#     print(f"{n} é multiplo de {mult}")
# else:
#     print(f"{n} não é múltiplo de {mult}") 

#12
# nome = input("Nome: ")
# disciplina = input("Disciplina: ")
# print("Informe suas notas!")
# n1 = float(input("Primeiro Bimestre: "))
# n2 = float(input("Segundo Bimestre: "))
# n3 = float(input("Terceiro Bimestre: "))
# n4 = float(input("Quarto Bimestre: "))
# pr = float(input("Provão: "))
# ed = float(input("Estudo Dirigido: "))
# media_n = (n1+n2+n3+n4) / 4
# print(f"Média aritmética de {disciplina}: {media_n}")
# media_final = ((media_n*0.2) + (ed*0.2) + (pr*0.6))
# if media_final >= 6:
#     print(f"----------{disciplina}----------\nAluno: {nome}\nNotas ->\nPrimeiro Bimestre: {n1}\nSegundo Bimestre: {n2}\nTerceiro Bimestre: {n3}\nQuarto Bimestre: {n4}\nProvão: {pr}\nEstudo Dirigido: {ed}\n-Média Final: {media_final}\n---Situação Final---\nO aluno {nome} foi APROVADO!")
# else:
#     print(f"----------{disciplina}----------\nAluno: {nome}\nNotas ->\nPrimeiro Bimestre: {n1}\nSegundo Bimestre: {n2}\nTerceiro Bimestre: {n3}\nQuarto Bimestre: {n4}\nProvão: {pr}\nEstudo Dirigido: {ed}\n-Média Final: {media_final}\n---Situação Final---\nO aluno {nome} foi REPROVADO!")


#2
# pedro = 1.50
# lucas = 1.10
# ano = 0

# while pedro > lucas:
#     pedro = pedro + 0.02 
#     lucas = lucas + 0.03
#     ano = ano + 1
# print(f"{ano} anos para terem a mesma altura")
# print(f"Lucas sera maior que pedro após {ano+1} anos")


# 3-TABUADA
# n = int(input('Digite um número para gerar a tabuada até ele: '))
# for contador in range(1, n + 1):
#         print(f'Tabuada do {contador}:')
#         for j in range(11):  # Para gerar a tabuada de 1 a 10
#             print(f'{contador} * {j} = {contador*j}')
#         print()  # Linha em branco entre as tabuadas


#4 
# a = int(input("Número inicial: "))
# b = int(input("Número final: "))
# quant_int_positivo = 0
# quant_pares = 0
# quant_impares = 0
# quant_impares_divisivel = 0
# soma1 = 0
# for contador in range(a , b + 1):
#     if contador > 0:
#         quant_int_positivo = quant_int_positivo + 1
#         soma1 = contador + contador
#     if contador % 2 == 0:
#         quant_pares = quant_pares + 1
#         soma2 = quant_pares + quant_pares
#     if contador % 2 != 0:
#         quant_impares = quant_impares + 1
#         soma3 = quant_impares + quant_impares
#     if contador % 2 != 0 and contador % 3 == 0 and contador % 7 == 0:
#         quant_impares_divisivel = quant_impares_divisivel + 1
#         soma4 = quant_impares_divisivel + quant_impares_divisivel
# #a)
# print(f"a) Quantidade de números inteiros: {quant_int_positivo}")
# #b)
# print(f"b) Quantidade de números ímpares: {quant_impares}")
# #c)
# print(f"c) Quantidade de números pares: {quant_pares}")
# #d)
# print(f"d) Quantidade de números ímpares e divisíveis por 3 e 7: {quant_impares_divisivel}")

# m_quant_int_positivo = soma1/quant_int_positivo
# m_quant_pares = soma2/quant_pares
# m_quant_impares = soma3/quant_impares
# m_quant_impares_divisivel = soma4/quant_impares_divisivel

# #e)
# print(f"e)\nMédia a = {m_quant_int_positivo:.2f}")
# print(f"Média a = {m_quant_pares:.2f}")
# print(f"Média a = {m_quant_impares:.2f}")
# print(f"Média a = {m_quant_impares_divisivel:.2f}")



#5
def gerar_fibonacci(x):

    sequencia = [1, 1]  
    contador = 2  
    
    while contador < x:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
        contador = contador + 1
    return sequencia


termos = int(input("Digite o número de termos que deseja na sequência de Fibonacci: "))
if termos > 0:
    fibonacci_sequencia = gerar_fibonacci(termos)
    print(f"Os primeiros {termos} termos da sequência de Fibonacci são:")
    print(fibonacci_sequencia)
else:
    print("Insira um número positivo e válido!")
