print("→Calculadora de Valores, By: L4MEK. 💘←")
#Usuario
nome = input("Digite seu nome: ")
#Info
print(f"\n{nome}, Use /info se tiver dúvidas.\n")

while True:
	
#Comandos
  valor = (input("🔥\n[1] KM - MI\n[2] MI - KM\n[3] CM - IN\n[4] IN - CM\n[5] KG - LB\n[6] LB - KG\n[7] C - F\n[8] F - C\n😝 R= "))
#Ajuda sobre os comandos
  if valor == "/info":
  	print ("\nDigite um número e aperte enter [1-8]\nKM = Quilômetro\nMI = Milha\nCM = Centímetro\nIN = Polegada\nKG = Quilo\nLB = Libra\nC = Graus Celsius\nF = Fahrenheit\n\n⭐ O código sera executado 3 vezes e depois vai parar.\nÉ possível mudar isso na sétima linha do código.")
	
#Quilômetros para Milhas
  elif valor == "1":
  	KM_p_MI = float(input(f"{nome}, Digite o valor em Quilômetros: "))
  	print(f"{KM_p_MI} Quilômetros em milhas é: ")
  	print (KM_p_MI / 1.609)
  	
  
#Milhas para Quilômetros
  elif valor == "2":
  	MI_p_KM = float(input(f"{nome}, Digite o valor em Milhas: "))
  	print(f"{MI_p_KM} Milhas em Quilômetros é: ")
  	print(MI_p_KM * 1.609)
	
#Centímetros em Polegadas
  elif valor == "3":
  	CM_p_IN = float(input(f"{nome}, Digite o valor em Centímetros: "))
  	print(f"{CM_p_IN} Centímetros em Polegadas é: ")
  	print(CM_p_IN / 2.54)

#Polegadas em Centímetros
  elif valor == "4":
  	IN_p_CM = float(input(f"{nome}, Digite o valor em Polegadas: "))
  	print(f"{IN_p_CM} Polegadas em Centímetros é: ")
  	print(IN_p_CM * 2.54)
	
#Quilo para Libra
  elif valor == "5":
  	KG_p_LB = float(input(f"{nome}, Digite o valor em Quilos: "))
  	print(f"{KG_p_LB} Quilos em Libras é:")
  	print(KG_p_LB * 2.20462262185)
	
#Libra para Quilo
  elif valor == "6":
  	LB_p_KG = float(input(f"{nome}, Digite o  valor em Libras: "))
  	print(f"{LB_p_KG} Libras em Quilos é:")
  	print(LB_p_KG / 2.20462262185)
  
#Celsius para Fahrenheit
  elif valor == "7":
  	valorcel = float(input("digite o valor em Graus Celsius (°C): "))
  	C_p_F = ((valorcel*9) / 5) + 32
  	saida2= round(C_p_F, 3)
  	print("{}ºC é {} ºF.".format(valorcel, C_p_F))
  
#Fahrenheit para Celsius
  elif valor == "8":
  	quantia = float (input("Digite o valor em Graus Fahrenheit (°F): "))
  	F_p_C= ((quantia-32)*5)/9
  	saida = round(F_p_C, 3)
  	print("{}ºF é {} ºC.".format(quantia,saida))
  elif valor == "9":
    break
