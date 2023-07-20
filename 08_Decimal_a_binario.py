# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

# Esta función toma un número decimal como entrada y lo convierte a su representación binaria.


# Esta función toma un número decimal como entrada y lo convierte a su representación binaria.
def transformar_decimal_a_binario(decimal):
    # Verifica si el número decimal es igual a 0
    if decimal == 0:
        # Si es así, devuelve 0 como la representación binaria
        return 0
    
    # Calcula el resto de la división del número decimal por 2
    # Esto da como resultado 0 o 1, que representa el bit menos significativo de la representación binaria
    resto = decimal % 2
    
    # Devuelve el resto calculado más el resultado de la llamada recursiva a la función con el número decimal dividido por 2
    # Multiplicado por 10 para desplazar los dígitos hacia la izquierda en la representación binaria
    return resto + 10 * transformar_decimal_a_binario(decimal // 2)

# Imprime la representación binaria del número decimal 100
print(transformar_decimal_a_binario(10))
