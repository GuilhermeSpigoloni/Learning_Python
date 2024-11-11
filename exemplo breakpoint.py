#calculador de fatorial simples
def calcular_fatorial(n):
    if n < 0:
        print(f"Fatorial não definido para números negativos:{n}")
        return None #Para números negativos, fatorial não é definido.
    
    resultado = 1
    for i in range(1, n + 1):
    #Condição para ativar o breackpoint
        if i == 0 or i < 0:
            breakpoint() #Vai parar aqui se a condição for satisfeita
        resultado *= i
    return resultado
numeros = {5, 7, 10, 0, 12, -3}
for numero in numeros:
    print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")