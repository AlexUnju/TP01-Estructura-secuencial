##Resuelva y muestre el valor y el tipo de las siguientes expresiones aritméticas y muestre los valores resultantes
##para x, y, z, pruebe con valores enteros para las variables de entrada.

x=float(input("Introduce el valor de x: "));
y=float(input("Introduce el valor de y: "));
z=float(input("Introduce el valor de z: "));
PI=3.1416;

e1 = 3*(x//y) +(-y//z)*5;
e2 = PI * x**2 - (1//2)*((x//y-z)**(1//3));

print("El valor de e1 es: "+str(round(e1,2))+ " y e2 es: " + str(round(e2,2)));