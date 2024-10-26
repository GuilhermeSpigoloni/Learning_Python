# EXTRA 
print("---Menu---\n1 - Inserir seus dados\n2 - Mês referente ao número")
escolha = input("Qual a boa: ")

if escolha == '1':
    class Pessoa():
            def __init__(self, apelido,sobrenome ,idade ,cidade ):
                self.apelido = apelido
                self.sobrenome = sobrenome
                self.idade = idade
                self.cidade = cidade

            def saida(self):
                print(f'---Essas são suas informações:--- \nNome: {self.apelido} {self.sobrenome}\nIdade: {self.idade}\nCidade: {self.cidade}')
    
    pessoa1 = Pessoa(input("Nome: "),input("Sobrenome:"),input("Idade: "),input("Cidade: "))
    pessoa1.saida()



elif escolha == '2':
# 02

    class Meses:
        
        def __init__(self,numero):
            self.numero = numero
            self.mes = ['Janeiro', 'Fevereiro', 'Março', 'Abriu', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
            
        def saida(self):

            if   1 <= self.numero <= 12:
                return self.mes [self.numero - 1]
            else:
                return "Invalido."

    numero = (int(input('Digite um número de 1 a 12: ')))
    mes = Meses(numero)
    print(f"O número {numero} é referente ao mês de {mes.saida()}")


        
else:
    print("Faça uma escolha válida!")










####################EXPLICAÇÃO####################


# class Vendedor:
#     def __init__(self,nome):
#         self.nome = nome

#     def informacaoSaida(self):
#         print(f"Olá, meu nome é {self.nome} e eu tenho")

# vendedor1 = Vendedor(input("Nome1: "))
# vendedor2 = Vendedor(input("Nome2: "))

# vendedor1.informacaoSaida()
# vendedor2.informacaoSaida()

# class Vendedor:
#     def __init__(self,nome,nome2,idade):
#         self.nome = nome
#         self.nome2 = nome2
#         self.idade = idade

#     def informacaoSaida(self):
#         print(f"Olá, meu nome é {self.nome} e meu sobrenome é {self.nome2} e eu tenho {self.idade} anos.")

# vendedor1 = Vendedor(input("Nome1: "),input("Sobrenome1: "),input("Idade1: "))
# vendedor2 = Vendedor(input("Nome2: "),input("Sobrenome2: "),input("Idade2: "))

# vendedor1.informacaoSaida()
# vendedor2.informacaoSaida()