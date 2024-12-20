#Escribe un programa que solicite al usuario un número entero positivo
#y luego calcule la suma de todos los números divisibles por 3 desde 1 hasta ese número utilizando un bucle while



numero = int(input("Introduce un número entero positivo: "))

suma = 0
i = 3  

while i <= numero:
    suma += i
    i += 3  


print("La suma de los números divisibles por 3 hasta", numero, "es:", suma)