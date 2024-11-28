# 6.5 and 6.6

ultimo1 = 10
ultimo2 = 5
fila1 = list(range(1,ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
operacao = 'qualquer coisa'
while operacao != 'S':
    print('------------------------------------------------')
    print(f'\nExistem {len(fila1)} clientes na fila normal\nExistem {len(fila2)} clientes na fila prioritária') 
    print('------------------------------------------------')
    print(f'Filas atuais:\nFila normal: {fila1}\nFila prioritária: {fila2}')
    print('------------------------------------------------')
    print(f'F - Finalizar atendimento\nA - Atendimento normal\nB - Atendimento prioditário\nS - sair.')
    print('------------------------------------------------')
    operacao = input('O que vai ser (F,A,B,S): ').upper()
    if operacao == 'A':
        ultimo1 += 1
        fila1.append(ultimo1)
    elif operacao == 'B':
        ultimo2 += 1
        fila2.append(ultimo2)
    elif operacao == 'F': 
        if len(fila1) > 0:
            atendido = fila1.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print('Fila vazia! Ninguém para atender!')
    elif operacao == 'S':
        print('Saindo...')
        break
    else:
        # from colorama import init, Fore
        # init()
        print('\n\nEscolha uma opção válida!\n\n')



