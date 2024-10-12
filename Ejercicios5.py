""" 
Nivel básico:
Verificar si un número es positivo, negativo o cero
Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

Determinar si un estudiante aprobó o no
Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.

Nivel intermedio:
Comprobar si un número es par o impar
Descripción: Crea un programa que pida al usuario un número y determine si es par o impar.

Verificar si un número está dentro de un rango
Descripción: Crea un programa que pida al usuario un número y verifique si está en el rango de 1 a 10 (inclusive). 
"""

pedro = 18
juan = 20

if pedro > juan:
    print("Pedro es mayor")
else:
    print("Juan es mayor")

def Aprobado(Calificacion):
    if Calificacion >= 5:
        print("Aprobado")
    else:
        print("Reprobado")
        
print("Determinar si un estudiante aprobó o no")
Calificacion = float(input("Ingresa la calificación: "))
Aprobado(Calificacion)

def ParImpar(Numero):
    if Numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

print("Comprobar si un número es par o impar")
Numero = int(input("Ingresa un numero:"))
ParImpar(Numero)

def Rango(numero):
    if numero >=1 and numero <= 10:
        print( "Esta en rango")
    else:
        print("No esta en rango")
print("Verificar si el numero esta en el rango")
numero =int(input("ingresa el numero: "))
Rango(numero)