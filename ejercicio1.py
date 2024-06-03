n = input("Introduce el dividendo (entero): ");
m = input("Introduce el divisor (entero): ");
print(n+" entre "+m+" da un cociente "+str(int(n)//int(m)) + " y un resto " + str(int(n)% int(m)));

# el valor que dara si n=2 y m=5 es cociente 0 y resto 2
# si m es cero el programa dara un error de division por cero
#el operador de resto que utiliza es % operador de modulo 
#si quito str dará error por concatenación de string con int
