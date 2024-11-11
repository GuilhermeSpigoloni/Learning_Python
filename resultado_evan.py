sim = True
nao = False
trabalho_terca = eval(input("Conseguiu o trabalho na terça? sim ou nao: "))
trabalho_quinta = eval(input("Conseguiu o trabalho na quinta? sim ou nao: "))

tv_85 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
saude = not sorvete

print(f"Trabalhei terça: {trabalho_terca}, trabalhei quinta: {trabalho_quinta}")
print("Comprei uma Tv 85': ", tv_85)
print("Comprei uma Tv 32': ", tv_32)
print("Comprei um Sorvete: ", sorvete)
print("Estou saudável: ", saude)
