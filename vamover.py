# lugares_vagos = [10,2,1,3,0]
# while True:
#     sala = int(input('Sala (0 sai): '))
#     if sala == 0:
#         print('Saindo...')
#         break
#     if sala > len(lugares_vagos) or sala < 1:
#         print('Sala inválida')
#     elif lugares_vagos[sala - 1] == 0:
#         print('Desculpe, sala lotado!')
#     else:
#         lugares = int(input(f'Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):'))
#         if lugares > lugares_vagos[sala - 1]:
#             print('Esse número de lugares não está disponível!')
#         elif lugares < 0:
#             print('Número inválido')
#         else:
#             lugares_vagos [sala - 1] -= lugares
#             print(f'{lugares} lugares vendidos')
# print('Utilização das salas')
# for sala, vagos in enumerate(lugares_vagos):
#     print(f'Sala {sala+1} - {vagos} lugar(es) vazio(s)')






# 6.14
# comprados = [0,0,0,0,0]
# lugares_vagos = [100,200,150,300,50]
# vendas_total = 0
# while True:
#     sala = int(input('Sala 1 a 5(0 sai): '))
#     if sala == 0:
#         print('Saindo...')
#         break
#     if sala > len(lugares_vagos) or sala < 1:
#         print('Sala inválida')
#     elif lugares_vagos[sala - 1] == 0:
#         print('Desculpe, sala lotado!')
#     else:
#         lugares = int(input(f'Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):'))
#         if lugares > lugares_vagos[sala - 1]:
#             print('Esse número de lugares não está disponível!')
#         elif lugares < 0:
#             print('Número inválido')
#         else:
#             lugares_vagos [sala - 1] -= lugares
#             comprados[sala -1 ] += lugares
#             vendas_total += lugares
#             print(f'{lugares} lugares vendidos')
# print('Utilização das salas')
# for sala, vagos in enumerate(lugares_vagos):
#     print(f'Sala {sala+1} - {vagos} lugar(es) vazio(s)')
# for sala, comprados in enumerate(comprados):
#     print(f'Ingressos vendidos\n Sala {sala+1} - {comprados}')
# print(f'Total de ingressos vendidos: {vendas_total}') 



# 6.15
qtd = int(input('Quantas salas terão: '))
qtdSalas = []
poltronas = 0
x = 0
while x < qtd:
    qtdSalas.append(qtd)
    poltronas = (input(f'Qualntas poltronas na sala {x+1}: '))
    qtdSalas.append(poltronas)
    x += 1
print(qtdSalas)
# comprados = [0,0,0,0,0]
# lugares_vagos = [10,2,1,3,0]
# vendas_total = 0
# while True:
#     sala = int(input('Sala 1 a 5(0 sai): '))
#     if sala == 0:
#         print('Saindo...')
#         break
#     if sala > len(lugares_vagos) or sala < 1:
#         print('Sala inválida')
#     elif lugares_vagos[sala - 1] == 0:
#         print('Desculpe, sala lotado!')
#     else:
#         lugares = int(input(f'Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):'))
#         if lugares > lugares_vagos[sala - 1]:
#             print('Esse número de lugares não está disponível!')
#         elif lugares < 0:
#             print('Número inválido')
#         else:
#             lugares_vagos [sala - 1] -= lugares
#             comprados[sala -1 ] += lugares
#             vendas_total += lugares
#             print(f'{lugares} lugares vendidos')
# print('Utilização das salas')
# for sala, vagos in enumerate(lugares_vagos):
#     print(f'Sala {sala+1} - {vagos} lugar(es) vazio(s)')
# for sala, comprados in enumerate(comprados):
#     print(f'Ingressos vendidos\n Sala {sala+1} - {comprados}')
# print(f'Total de ingressos vendidos: {vendas_total}') 
