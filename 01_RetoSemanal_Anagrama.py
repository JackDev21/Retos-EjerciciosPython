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


def anagrama(): # Definimos una funcion llamada anagrama.
    print(anagrama1("amor", "roma")) # Llamamos a la funcion anagrama con dos palabras.
    

def anagrama1(palabra1, palabra2): 
    print("Palabra 1: ", palabra1) # En este paso hacemos print para ver que palabras son.
    print("Palabra 2: ", palabra2)

    if palabra1.lower() == palabra2.lower(): # Lower convierte todo texto escrito a minuscula. Y verificamos si son iguales para que retorne false.
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower()) # sorted ordena los caracteres de la palabra en orden alfabetico y devuelve 
                                                        # una lista de caracteres ordenados. Se compara si son iguales y si tienen
                                                        # las mismas letras y consonantes ordenadas es un anagrama y devuelve True.

anagrama() # Aqui llamamos a la funcion anagrama para ejecutar el programa.
