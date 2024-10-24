# EXTRA 
print("---Menu---\n1 - Inserir seus dados\n2 - Mês referente ao número")
escolha = input("Qual a boa: ")

if escolha == '1':
#01
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")
    lista = [nome, sobrenome, idade, cidade]
    print(f'Essas são suas informações: {lista}')

elif escolha == '2':
# 02

    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abriu', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    a = int(input('Digite um número de 1 a 12: '))
    if a >= 1 and a <= 12:
        a = a-1
        print(meses[a])
    else:
        print("ERRO! Digite um número de 1 a 12.")
        
else:
    print("Faça uma escolha válida!")