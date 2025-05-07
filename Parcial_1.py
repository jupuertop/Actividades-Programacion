#Parcial 1
#Suma de pares positivos
#5 numeros enteros e identificar cuales son positivos y enteros.
             

suma = 0

for i in range(5):
     numero = int(input("Ingrese un numero entero: "))

     if numero > 0 and numero % 2 == 0:
          suma += numero

print(f"La suma de los pares positivos es:{suma}")
#Clasificacion de edad

def calificacion_edad():
     entrada = input("Ingrese la edad:") 

     if not entrada.isdigit():
          print("La edad no puede ser un numero entero negativo. ")
          return
     edad = int(entrada)

     if edad <= 0:
          print("La edad no puede ser un numero entero negativo. ")
     elif edad < 13:
          print("Niño")
     elif 13 <= edad <= 17:
          print("Adolescente")
     elif 18<= edad <= 59:
          print("Adulto")
     else:
          print("Adulto mayor")

          







