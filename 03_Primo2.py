# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for divisible in range(2, num):
        if num % divisible == 0:
            return False
    else:
        return True

lista_primo = [] # Lista vacía para almacenar los números primos

# Solicita al usuario que ingrese un número para comprobar si es primo y lo guarda en la variable "numero_usuario"
numero_usuario = int(input("Ingrese un número para comprobar si es primo: "))

if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")

# Imprime los números primos entre 1 y 100
print("Los números primos entre 1 y 100 son:")
for numero in range(1, 101):
    if es_primo(numero):
        lista_primo.append(numero)

print(lista_primo)
