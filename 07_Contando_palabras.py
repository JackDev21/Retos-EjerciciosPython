
# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
#   lo resuelvan automáticamente.

import re

# Este código importa el módulo 're', que proporciona soporte para expresiones regulares en Python.

def recuento(palabra):
    # Esta función toma una cadena como entrada y cuenta la frecuencia de cada palabra en la cadena.
    
    palabra = palabra.lower()
    # Esta línea convierte todos los caracteres de la cadena a minúsculas.
    
    palabras = re.findall(r'\b\w+\b', palabra)
    # Esta línea utiliza la función 'findall' del módulo 're' para encontrar todas las palabras en la cadena.
    # La expresión regular '\b\w+\b' coincide con cualquier carácter de palabra (\w) rodeado de límites de palabra (\b).
    # El resultado es una lista de todas las palabras encontradas en la cadena.
    
    diccionario = {}
    # Esta línea inicializa un diccionario vacío para almacenar las frecuencias de las palabras.
    
    for palabra in palabras:
        # Este bucle itera sobre cada palabra en la lista 'palabras'.
        
        if palabra not in diccionario:
            # Si la palabra no es una clave en el diccionario, se agrega con un valor de 1.
            
            diccionario[palabra] = 1
        else:
            # Si la palabra ya es una clave en el diccionario, se incrementa su valor en 1.
            
            diccionario[palabra] += 1

    return diccionario
    # Esta línea devuelve el diccionario final que contiene las frecuencias de las palabras.


palabra = input("Ingrese una frase con palabras repetidas: ")
# Esta línea solicita al usuario que ingrese una frase con palabras repetidas y la almacena en la variable 'palabra'.

print(recuento(palabra))
# Esta línea llama a la función 'recuento' con la entrada del usuario e imprime el diccionario resultante de las frecuencias de las palabras.
