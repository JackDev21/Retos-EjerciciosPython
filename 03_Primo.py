# Programa para comprobar si un número es o no primo.
# Imprime los números primos entre 1 y 100.

# Define una función llamada "es_primo" que determina si un número es primo o no.
def es_primo(numero):
    if numero <= 1:  # Numeros menores o iguales a 1 no son primos.
        return False
    for i in range(2, int(numero ** 0.5) + 1):  # Itera desde 2 hasta la raiz cuadrada del numero dado más 1.
        if numero % i == 0:  # Si el número es divisible por algún número en este rango, no es primo.
            return False
    return True

# Solicita al usuario que ingrese un número para comprobar si es primo y lo guarda en la variable "numero_usuario"
numero_usuario = int(input("Ingrese un número para comprobar si es primo: "))

# Comprueba si el número ingresado por el usuario es primo utilizando la función "es_primo"
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")

# Imprime los números primos entre 1 y 100
print("Los números primos entre 1 y 100 son:")
for numero in range(1, 101):
    if es_primo(numero):  # Comprueba si cada número en el rango es primo utilizando la función "es_primo"
        print(numero,end=" ")
