#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def Conversor():
    resultado_loop = "s"
    
    while resultado_loop.upper() == "S":
        print("CONVERTOR DE TEMPERATURA")
        escolha = input("Escolha:\n 1-Celsius para Fahrenheit\n 2-Fahrenheit para Celsius\n")

        if escolha == "1":
            grausC = float(input("Graus em Celsius (°C): "))
            resultado = (grausC * 9/5) + 32
            print(f"{resultado:.2f}")

        elif escolha == "2":
            grausF = float(input("Graus Fahrenheit (°F): "))
            resultado = 5 * ((grausF - 32) / 9)
            print(f"{resultado:.2f}")

        else:
            print("Faça uma escolha válida!")


    resultado_loop = input("\n\nDeseja converter outro número? (S/N)")
            
Conversor()