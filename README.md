# TP01-Estructura-secuencial
## **Casos de Estudio**
Analice, diseñe y codifique los siguientes enunciados en Python
##
### 1. Calcular el volumen de una esfera cuya fórmula es:  $\Large{𝑣 = \frac{4}{3}π𝑟^3}$
#### Resolución:
```python
PI = 3.1416;
radio = float(input("escriba el valor de radio: "))
volumen = 4/3*PI*radio**3;
print('El volumen de la esfera es de '+ (round(volumen,2))+' unidades de volumen.')
```
##
### 2. Dados el precio de un producto y el número de unidades a comprar, muestre el importe de dinero a pagar
#### Resolución:
```python
precio= int(input("ingrese el precio del producto "));
unidades= int(input("ingrese la cantidad de unidades a comprar "));

importePago = precio * unidades;
print("el importe a pagar es: ",importePago);
```


## Ejercicios
### 1. Dado el siguiente código en Python: <br>
```python
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n+" entre "+m+" da un cociente "+str(int(n)//int(m)) + " y un resto " + str(int(n) % int(m)))
```

- Muestre el resultado con n = 2 y m = 5
- ¿Puede obtener un resultado para cualquier valor de m?
- ¿Qué operador utiliza para calcular el resto?
- Modifique el código quitando str() en la 3er línea, ¿qué sucede?
#### Resolución:
```python
# el valor que dara si n=2 y m=5 es cociente 0 y resto 2
# si m es cero el programa dara un error de division por cero
#el operador de resto que utiliza es % operador de modulo 
#si quito str dará error por concatenación de string con int
```
##


### 2. Resuelva y muestre el valor y el tipo de las siguientes expresiones aritméticas y muestre los valores resultantes
para x, y, z, pruebe con valores enteros para las variables de entrada.

|   |   |
|---|---|
| $$\Large{𝑒_1 = 3\frac{x}{y} + \frac{-y}{z}5}$$ | $$\Large{𝑒_2 = \pi x^2 - \frac{1}{2}\sqrt[3]{\frac{x}{y-z}}}$$ |

#### Resolución:
```python
x=float(input("Introduce el valor de x: "));
y=float(input("Introduce el valor de y: "));
z=float(input("Introduce el valor de z: "));
PI=3.1416;

e1 = 3*(x//y) +(-y//z)*5;
e2 = PI * x**2 - (1//2)*((x//y-z)**(1//3));

print("El valor de e1 es: "+str(round(e1,2))+ " y e2 es: " + str(round(e2,2)));
```
##

### 3. Tienes una nueva cuenta de caja de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden al final del período. Escribir un algoritmo que
comience leyendo la cantidad de dinero depositada en la cuenta de ahorros. Calcular y mostrar por pantalla la
cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. Ejemplo
de ejecución para una cantidad de dinero depositada de 12896

| Cantidad de dinero | Ahorros 1er año | Ahorros 2do año | Ahorros 3er año |
|---------------------|------------------|------------------|------------------|
| 12896               | 13411.84         | 13948.31         | 14506.2           |

#### Resolución:

```python
dineroDepositado=int(input("ingrese el dinero depositado: "));
interes=0.04;
primerAnioAhorro= dineroDepositado + dineroDepositado*interes;
segundoAnioAhorro= primerAnioAhorro + primerAnioAhorro*interes;
tercerAnioAhorro= segundoAnioAhorro + segundoAnioAhorro*interes;

print("El primer año de ahorro es: "+str(round(primerAnioAhorro,2))+ " el segundo año de ahorro es: " + str(round(segundoAnioAhorro,2))+ " el tercer año de ahorro es: " + str(round(tercerAnioAhorro,2)));
```

##

### 4. Calcule el perímetro y la superficie de un rectángulo solicitando al usuario la longitud de sus lados.
####Resolucón:
```python
base=int(input("ingrese la base "));
altura=int(input("ingrese la altura "));
superficie= base*altura;
perimetro=2*altura+2*base;

print("el perimetro es: "+str(perimetro)+ " y la superficie es de:"+str(superficie));
```
##

### 5. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#### Resolución:
```python
catetoA=int(input("ingrese el cateto A "));
catetoB=int(input("ingrese el cateto B "));

hipotenusa= (catetoA**2 + catetoB**2)**(1/2);
print("la hipotenusa es: "+str(round(hipotenusa,2)));
```
##
### 6. Solicite el ingreso de una cantidad de pesos Argentinos, dar su equivalente en dólares y en euros. Se sabe que 1 dólar = 202,30 pesos y 1 euro = 214,30 pesos (formatee los resultados a 3 decimales).
#### Resolución:
```python
pesos=float(input("ingrese la cantidad de pesos a convertir: "));
dolar=float(input("ingrese el valor del dolar: "));
euro=float(input("ingrese el valor del euro: "));

conversionPesosDolar= pesos/dolar;
print("la conversion de pesos a dolar es: "+str(round(conversionPesosDolar,3))+ " y la conversion de pesos a euro es: "+str(round(pesos/euro,3)));
```
##
### 7. Solicite el valor de un ángulo en Radianes conviértalo a grados Sexagesimales y luego a Centesimales. 

Muestre los resultados en pantalla. Fórmula de conversiones: 
sexadecimal = valorEnRadian * 180 / Pi, centesimal = valorEnRadian * 200 / Pi

#### Resolución:
```python
radianes=float(input("ingrese el valor en radianes: "));
PI=3.1416;

sexadecimal = radianes * 180 / PI;
centesimal = radianes * 200 / PI;

print("el valor en sexadecimal es: "+str(round(sexadecimal,2))+ " y el valor en centesimal es: "+str(round(centesimal,2)));
```
##
### 8. Determine la distancia entre dos puntos en el espacio. Punto 1: (x1, y1, z1) y Punto 2: (x2, y2, z2).
$$
\Large{d=\sqrt{(\mathbf{x}_2 - \mathbf{x}_1)^2 + (\mathbf{y}_2 - \mathbf{y}_1)^2 + (\mathbf{z}_2 - \mathbf{z}_1)^2}}
$$

#### Resolución:
```python
x1=int(input("ingrese la coordenada x1 "));
y1=int(input("ingrese la coordenada y1 "));
z1=int(input("ingrese la coordenada z1 "));
x2=int(input("ingrese la coordenada x2 "));
y2=int(input("ingrese la coordenada y2 "));
z2=int(input("ingrese la coordenada z2 "));

distancia= ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(1/2);

print("la distancia entre los puntos es: "+str(round(distancia,2)));
```
##
### 9. Diseñar un programa que permita calcular el índice de masa corporal de una persona.
#### Resolución:
```python
peso=float(input("ingrese el peso en kg: "));
altura=float(input("ingrese la altura en metros: "));

IMC= peso/(altura**2);

print("su indice de masa corporal es: "+str(round(IMC,2)));
```








