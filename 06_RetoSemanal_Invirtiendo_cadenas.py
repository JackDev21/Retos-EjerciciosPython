
# Reto #6
# INVIRTIENDO CADENAS
# Fecha publicación enunciado: 07/02/22
# Fecha publicación resolución: 14/02/22
# Dificultad: FÁCIL
#
# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

# Primero, se define la función Palabra_Invertida con un parámetro llamado cadena, que representa la cadena de texto que se desea invertir.
def Palabra_Invertida(cadena):
    # Creamos una cadena vacía para almacenar la cadena de texto invertida
    cadena_invertida = ""

    # Iteramos sobre cada letra en la cadena original
    for letra in cadena:
        # Agregamos cada letra al inicio de la cadena invertida, si fuera cadena_invertida + letra se quedaria igual la palabra.
        cadena_invertida = letra + cadena_invertida
    # Devolvemos la cadena invertida
    return cadena_invertida

# Llamamos a la función Palabra_Invertida con la cadena "Hola Mundo" como argumento
print(Palabra_Invertida("Hola Mundo"))
