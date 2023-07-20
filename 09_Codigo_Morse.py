
# Crea un programa que sea capaz de transformar texto natural a código
# morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
#   la conversión.
# - En morse se soporta raya "-", punto ".", un espacio " " entre letras
#   o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
#   https://es.wikipedia.org/wiki/Código_morse.


 #Definimos una función llamada "transformar_a_morse" que toma un parámetro llamado "texto"
def transformar_a_morse(texto):
    # Creamos un diccionario que contiene las equivalencias entre letras y su representación en código Morse
    morse = {
        "a": ".-", # Letras en código Morse
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        " ": " ", # Espacio en blanco en código Morse
    }

    if "." in texto or "-" in texto:
        # Si el texto contiene puntos o guiones, es que es código Morse y lo convertimos a texto natural
        resultado = ""  # Variable para almacenar el resultado de la conversión
        codigo_morse = texto.split(" ")  # Dividimos el texto en una lista de códigos Morse separados por espacios
        for codigo in codigo_morse:  # Recorremos cada código Morse en la lista
            for letra, morse_codigo in morse.items():  # Recorremos el diccionario "morse"
                if codigo == morse_codigo:  # Si encontramos una coincidencia entre el código Morse y su representación en el diccionario
                    resultado = resultado + letra  # Agregamos la letra correspondiente al resultado
                    break  # Salimos del bucle interno
            else:
                resultado = resultado + " "  # Si no encontramos una coincidencia, agregamos un espacio en blanco al resultado
    else:
        # Si el texto no contiene puntos ni guiones, asumimos que es texto natural y lo convertimos a código Morse
        resultado = ""  # Variable para almacenar el resultado de la conversión
        for letra in texto:  # Recorremos cada letra en el texto
            if letra.lower() in morse:  # Verificamos si la letra está presente en el diccionario "morse" (ignorando mayúsculas/minúsculas)
                resultado = resultado + morse[letra.lower()] + " "  # Agregamos la representación en código Morse al resultado
            else:
                resultado = resultado + " "  # Si la letra no está presente en el diccionario, agregamos un espacio en blanco al resultado

    return resultado.strip()  # Devolvemos el resultado de la conversión eliminando los espacios en blanco al principio y al final

texto = input("Ingrese el texto a transformar: ")  # Solicitamos al usuario que ingrese el texto a transformar y lo guardamos en la variable "texto"
resultado = transformar_a_morse(texto)  # Llamamos a la función "transformar_a_morse" pasando el texto como argumento y guardamos el resultado en la variable "resultado"
print(resultado)  # Imprimimos el resultado de la conversión en la consola
