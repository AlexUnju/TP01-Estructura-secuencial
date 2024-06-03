radianes=float(input("ingrese el valor en radianes: "));
PI=3.1416;

sexadecimal = radianes * 180 / PI;
centesimal = radianes * 200 / PI;

print("el valor en sexadecimal es: "+str(round(sexadecimal,2))+ " y el valor en centesimal es: "+str(round(centesimal,2)));