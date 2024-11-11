#exercício_depuração.py

def soma_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def media_lista(lista):
        soma = soma_lista(lista)
        media = soma / len(lista)
        return media

dados = [10,20,30,40]
print(f"A soma é: {soma_lista(dados)}")
print(f"A média é: {media_lista(dados)}")
