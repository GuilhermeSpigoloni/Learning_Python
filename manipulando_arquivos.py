# #Criar o arquivo
# arquivo = open('numero.txt','w')
# for linha in range (1,101):
#     arquivo.write(f'{linha}\n')
# arquivo.close


# #Abrir o arquivo
# arquivo = open('numero.txt', 'r')
# for linha in arquivo.readlines():
#     print(linha)
# arquivo.close


# #Outra forma de abrir
# with open('numero.txt' 'r') as arquivo:
#     for linha in arquivo.readlines():
#         print(linha)
        

#Criando duas pastas, impares e pares
with open('impares.txt', 'w') as impares:
    with open('pares.txt', 'w') as pares:
        for n in range(0,1001):
            if n % 2 == 0:
                pares.write(f'{n}\n')
            else:
                impares.write(f'{n}\n')