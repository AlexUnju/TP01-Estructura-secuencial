peso=float(input("ingrese el peso en kg: "));
altura=float(input("ingrese la altura en metros: "));

IMC= peso/(altura**2);

print("su indice de masa corporal es: "+str(round(IMC,2)));