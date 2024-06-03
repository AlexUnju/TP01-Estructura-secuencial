pesos=float(input("ingrese la cantidad de pesos a convertir: "));
dolar=float(input("ingrese el valor del dolar: "));
euro=float(input("ingrese el valor del euro: "));

conversionPesosDolar= pesos/dolar;
print("la conversion de pesos a dolar es: "+str(round(conversionPesosDolar,3))+ " y la conversion de pesos a euro es: "+str(round(pesos/euro,3)));
