
trabalho_terca = eval(input("Conseguiu o trabalho na terça? True ou Falso: "))
trabalho_quinta = eval(input("Conseguiu o trabalho na quinta? True ou Falso: "))

tv_85 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
saude = not sorvete

print("Tv 85' = ", tv_85)
print("Tv 32' = ", tv_32)
print("Sorvete = ", sorvete)
print("Saude = ", saude)
print(type(trabalho_terca))
print(type(trabalho_quinta))