import random
import time
import os

quant_num = int(input("Quantos números serão sorteados: "))
inicio = int(input("Início: "))
fim = int(input('Fim: '))

os.system('cls')

x = 0
soma = 0
print(f"----------Números Sorteados {quant_num} ----------")
while x < quant_num:
    x += 1
    sorteio = random.randint(inicio,fim)
    soma += sorteio
    print(f" {sorteio} -", sep='-' ,end='',flush=True)  
    time.sleep(1)

print('\n------------------------------------------')
print("A soma está sendo feita...")
time.sleep(1)
print(f'A soma do sorteio é: {soma}')
print('------------------------------------------')