# l = []
# l.append ('elemento que ira entrar na lista')
# print(l)
# print(len(l))

# lista = []

# while True:
#     n = int(input('Digite um número ou 0 para sair: '))
#     if n == 0:
#         break
#     lista.append(n)
    


# x = 0

# while x < len(lista):
#     print(lista[x])
#     x += 1






# ### 6.2

# lista1 = []
# lista2 = []


# while True:
#     e = int(input("Valor(es) a ser adicionado a primeira lista(0 pra finalizar): "))
#     if e == 0:
#         break
#     lista1.append(e)
    
# while True:
#     ee = int(input("Valor(es) a ser adicionado a segunda lista(0 pra finalizar): "))
#     if ee == 0:
#             break
#     lista2.append(ee)
    
    
# lista3 = []
# lista1.extend(lista2)
# lista3.extend(lista1)
# print(lista3)



# ### 6.3
# lista1 = []
# lista2 = []


# while True:
#     e = int(input("Valor(es) a ser adicionado a primeira lista(0 pra finalizar): "))
#     if e == 0:
#         break
#     lista1.append(e)
    
# while True:
#     ee = int(input("Valor(es) a ser adicionado a segunda lista(0 pra finalizar): "))
#     if ee == 0:
#             break
#     lista2.append(ee)
    
# lista3 = list(set(lista1) | set(lista2))
# print(lista3) 
