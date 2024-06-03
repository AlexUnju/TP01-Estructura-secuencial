x1=int(input("ingrese la coordenada x1 "));
y1=int(input("ingrese la coordenada y1 "));
z1=int(input("ingrese la coordenada z1 "));
x2=int(input("ingrese la coordenada x2 "));
y2=int(input("ingrese la coordenada y2 "));
z2=int(input("ingrese la coordenada z2 "));

distancia= ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(1/2);

print("la distancia entre los puntos es: "+str(round(distancia,2)));
