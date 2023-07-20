#Reto #1
#¿ES UN ANAGRAMA? Fecha publicación enunciado: 03/01/22
#Fecha publicación resolución: 10/01/22
#Dificultad: MEDIA
#Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#NO hace falta comprobar que ambas palabras existan.
#Dos palabras exactamente iguales no son anagrama.

# Reto #1
# ¿ES UN ANAGRAMA?
# Dificultad: MEDIA

# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

# Solicita al usuario que ingrese la primera palabra y la guarda en la variable "palabra1"
palabra1 = input("Escribe la primera palabra: ")

# Solicita al usuario que ingrese la segunda palabra y la guarda en la variable "palabra2"
palabra2 = input("Escribe la segunda palabra: ")

# Define una función llamada "es_anagrama" que toma dos palabras como argumentos
def es_anagrama(palabra1, palabra2):
    # Compara si las palabras son anagramas, ordenando sus caracteres y verificando si son iguales
    return sorted(palabra1) == sorted(palabra2)

# Llama a la función "es_anagrama" pasando las palabras ingresadas por el usuario y guarda el resultado en la variable "resultado"
resultado = es_anagrama(palabra1, palabra2)

# Imprime el resultado (True o False) que indica si las palabras son anagramas o no
print(resultado)
