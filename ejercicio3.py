dineroDepositado=int(input("ingrese el dinero depositado: "));
interes=0.04;
primerAnioAhorro= dineroDepositado + dineroDepositado*interes;
segundoAnioAhorro= primerAnioAhorro + primerAnioAhorro*interes;
tercerAnioAhorro= segundoAnioAhorro + segundoAnioAhorro*interes;

print("El primer año de ahorro es: "+str(round(primerAnioAhorro,2))+ " el segundo año de ahorro es: " + str(round(segundoAnioAhorro,2))+ " el tercer año de ahorro es: " + str(round(tercerAnioAhorro,2)));