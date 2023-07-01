# En este código se comprueba si es primo sin la funcion "def" definir

# Verificar si un número es primo
numero_usuario = int(input("Ingrese un número para comprobar si es primo: "))

if numero_usuario <= 1:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(numero_usuario ** 0.5) + 1):
        if numero_usuario % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")

# Imprimir los números primos entre 1 y 100
print("Los números primos entre 1 y 100 son:")
for numero in range(1, 101):
    if numero <= 1:
        es_primo = False
    else:
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
    if es_primo:
        print(numero, end=" ")