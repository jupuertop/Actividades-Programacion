#Escribir un programa que sume los cuadrados de los cien primeros números naturales
suma = 0
dato = 1
while(dato <= 100):
    suma += dato*dato
    dato += 1
    print(f"suma de los primeros 100 números naturales es: {suma}")

#número entero desde teclado y realiza la suma de los 100 numeros siguientes
numero = int(input("ingresa un numero entero positivo:  "))

if numero >= 0: 
    suma = 0
    for i in range(numero + 1, numero + 101):
        suma += i
    print("la suma de los 100 numeros siguientes es:" , suma)
else:
    print("El numero debe ser positivo. Intentar de nuevo")

#Convertir de euros a dolares
# 1 euro = 1.13 dolares

tipo_cambio = 1.120

euros = float(input("Ingresa la cantidad de euros: "))

if euros >= 0:
    dolares = euros * tipo_cambio
    print(f"{euros} euros equivalen a {dolares:.2f} dolares.")
else:
    print("la cantidad no puede ser negativa")

#Calcular el area d eun rectangulo
altura = float(input("Ingresa la altura del rectangulo: "))
anchura = float(input("Ingresa la anchura del rectangulo: "))

if altura > 0 and anchura > 0:
    area = altura * anchura
    print(f"El area del rectangulo es: {area}")
else:
    print("La altura y la anchura deben ser numeros positivos")

#Dos numeros del teclado, cual es menor y cual es mayor

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El numeor mayor es: {num1}")
    print(f"El numero menor es: {num2}")
elif num2 > num1:
    print(f"El numero mayor es: {num2}")
    print(f"El numero menor es: {num1}")
else:
    print("Ambos numeros son iguales.")

#Número entero por teclado e imprimir los numeros impares menores que el
numero = int(input("Ingrese un número entero: "))

print(f"Números impares menores que {numero}:")
for i in range(1, numero):
    if i % 2!= 0:
        print(i)

#Algoritmo de Euclides para encontrar gcd de numeros leidos desde el teclado
z = int(input("Ingresa el primer numero: "))
n = int(input("Ingrese el segundo numero: "))

while n != 0:
    z, n = n, z % n

print(f"EL maximo común divisor es: {z}")

#Ecuacion de segundo con coeficientes a, b y c

import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0:
    print("No es una ecuacion de segundo grado.")
else:
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("Dos soluciones reales:", x1, "y", x2)
    elif d== 0:
        x = -b / (2*a)
        print("Una solucion real:", x)
    else:
        print("No tiene soluciones reales")



