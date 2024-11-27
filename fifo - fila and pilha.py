# ordemChegada = [1,2,3,4,5,6,7,8,9,10]
# print(ordemChegada)
# ordemChegada.append(11)
# print(ordemChegada)
# ordemChegada.pop(0)
# print(ordemChegada)

## FILA ##

# ultimo = 10
# fila = list(range(1, ultimo + 1))
# 
# while True:
    # print(f'Há {len(fila)} pessoas na fila!')
    # print(f'Fila atual: {fila}')
    # print(f'----------------------------')
    # print('1 - Entrar na fila\n2 - Já é sua vez? Seja atendido\n 3 - Finalizar atendimento')
    # print(f'----------------------------')
    # escolha = int(input('Insira o número correspondente ao que deseja: '))
    # if escolha == 1:
        # ultimo += 1
        # fila.append(ultimo)
    # elif escolha == 2:
        # if len(fila) > 0:
            # atendido = fila.pop(0)
            # print(f'Atendimento realizado, Até a próxima {atendido}')
        # else:
            # print('A fila está vazia, Retorne ao menu e entre na fila')
    # elif escolha == 3:
        # print('Até a próxima...')
        # break
    # else:
        # print(f'{escolha} essa é uma opção inválida! Insira: 1, 2 ou 3.')
        
        

## PILHA ##

# pratos = 5
# pilha = list(range(1, pratos + 1))

# while True:
    # print(f'Existem {len(pilha)} pratos na pilha')
    # print(f'Pilha atual: {pilha}')
    # print(f'----------------------------')
    # print(f'1 - Adicionar prato\n2 - Lavou um prato \n3 - Pratos limpos, Tchau!')
    # print(f'----------------------------')
    # escolha = int(input('Ação a ser realizada: '))
    # if escolha == 1:
        # pratos += 1
        # pilha.append(pratos)
    # elif escolha == 2:
        # pilha.pop(-1)
    # elif escolha == 3:
        # print(f'Finalmente o descanso...')
        # break
    # else:
        # print('Escolha inválida, retorne ao menu e digite uma ação válida!')
        


        
## BUSCAR ITEM NA LISTA ##

# 
# L = [1 , 2, 3, 4, 5]
# p = int(input('Digite o valor a procurar: '))
# achou = False
# x = 0
# while x < len(L):
    # if L[x] == p:
        # achou = True
        # break
    # x += 1
    # 
# if achou: 
    # print(f'{p} achado na posição {x}')
# else: 
    # print(f'Elemento {p} não encontrado!')