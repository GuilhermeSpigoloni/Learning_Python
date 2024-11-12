# import time

# x = 10 
# while x >= 0:
#     print(f'Decolagem em: {x}')   
#     time.sleep(1)
#     x -= 1

# print("Decolar!")

# fim = float(input("Último número a ser impresso: "))
# comeco = float(input("Começo: "))
# passo = float(input("De quandos em quantos números: "))

# while comeco <= fim:

#     if comeco % 2 == 0:
#         print(f"O número {comeco:.2f} é par!")
#     else:
#         print(f'O número {comeco:.2f} é ímpar!')

#     time.sleep(0.25)
#     comeco += 1

# print("Fim!")


# nota = 0 
# questao = 1
# while questao <= 5:
#     resposta = input(f"Resposta para a questão {questao}: ")
#     if questao == 1 and resposta == 'a':
#         nota += 1
#     if questao == 2 and resposta == 'a':
#         nota += 1
#     if questao == 3 and resposta == 'a':
#         nota += 1
#     if questao == 4 and resposta == 'a':
#         nota += 1
#     if questao == 5 and resposta == 'a':
#         nota += 1
    
#     questao += 1

# print(f"O aluno fez {nota} ponto(s)!")


contador = 0
soma = 0
resposta = 's'

while resposta != 'n':
        contador += 1
        idade = int(input(f"Idade da pessoa {contador}: "))
        soma += idade
        resposta = input("Tem mais pessoas na sala(s/n): ")

media = soma/contador
print(f"Relatório final: \nNúmero de participantes: {contador}\nSoma das idades: {soma}\nMédia das idades: {media}")

