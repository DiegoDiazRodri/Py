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

Nivel Avanzado:

Clasificación de Números
    Descripción: Crea una función que reciba una lista de números enteros y clasifique cada número como "positivo", "negativo" o "cero". La función debe devolver un diccionario que contenga el conteo de cada categoría.

    Requisitos:

    Utilizar if, elif y else para clasificar los números.
    Deberá considerar si el número es impar o par, y agregar esta información al diccionario.

Cálculo de Tarifas de Envío
    Descripción: Diseña una función que calcule la tarifa de envío basada en el peso del paquete y el destino. La tarifa debe ser calculada usando las siguientes reglas:

    Menos de 1 kg: $5
    De 1 a 5 kg: $10
    Más de 5 kg: $20
    Si el destino es internacional, sumar un recargo del 50% al costo total.
    Requisitos:

Usa if y else para determinar el costo según el peso.
Usa if adicional para comprobar si el envío es internacional y calcular el recargo correspondiente.
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

def Numeros(numero):
    if numero > 0:
        print("es positivo")
    else:
        print("es negativo")

print("Verificar si el numero es positivo o negativo")
numero =int(input("ingresa el numero: "))
Numeros(numero)