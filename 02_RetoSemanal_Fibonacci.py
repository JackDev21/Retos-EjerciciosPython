# Reto #2
# LA SUCESIÓN DE FIBONACCI
# Dificultad: DIFÍCIL

# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

n0 = 0 # Le damos valor a la variable
n1 = 1 # Le damos valor 1 a la variable

for i in range (0, 51): # Iteramos los 50 primeros numeros en "i" se ejecuta 50 veces.

    print(n0) # Aqui imprimimos el primer valor de la variable para empezar el ciclo.
    total = n0 + n1 # Se hace la suma y se guarda en la variable total
    n0 = n1 # Se actualiza la variable n0 a n1 modificanto su valor para que continue el ciclo.
    n1 = total # n1 se actualiza a el valor que da el resultado almacenado en el total
    