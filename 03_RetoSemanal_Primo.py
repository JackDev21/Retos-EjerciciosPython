# Programa para comprobar si un número es o no primo.
# Imprime los números primos entre 1 y 100.

def es_primo(numero):
    
    # Función que determina si un número es primo o no.
    if numero <= 1: # Numeros menores o iguales a 1 no son primos.  
        return False
    for i in range(2, int(numero ** 0.5) + 1): # Formula que itera desde 2 hasta la raiz cuadrada del numero dado más 1. No es primo
        if numero % i == 0:
            return False
    return True

# Preguntamos al usuario si quiere comprobar si un número es primo
numero_usuario = int(input("Ingrese un número para comprobar si es primo: "))
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")

# Imprimimos los números primos entre 1 y 100
print("Los números primos entre 1 y 100 son:")
for numero in range(1, 101):
    if es_primo(numero):
        print(numero,end= " ")
