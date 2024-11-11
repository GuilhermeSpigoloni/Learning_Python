#Calculadora em python
def calculadora():
    
    #Entrada de dados
    num1 = float (input("Digite o primeiro número: "))
    operacao = (input("Escolha a operação (+,-,*,/)"))
    num2= float (input("Digite o segundo número: "))


    #Processamento e saída
    if operacao == "+":
        resultado = num1 + num2
        print("Resultado: ", resultado)

    elif operacao == "-":
        resultado = num1 - num2
        print("Resultado: ", resultado)

    elif operacao == "*":
        resultado = num1 * num2
        print("Resultado: ", resultado)
    
    elif operacao == "*":
        resultado = num1 * num2
        print("Resultado: ", resultado)

    elif operacao == "/":
        if num2 !="0":
            resultado = num1 / num2
            print("Resultado: ", resultado)
        else:
            print("Erro, / por 0 não existe.")
    
    else:
        print("Operaçao inválida.")

    
# Executa a função calculadora
calculadora()
        
