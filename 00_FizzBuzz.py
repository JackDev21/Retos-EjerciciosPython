"""
package com.mouredev.weeklychallenge2022

/*
 * Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 03/01/22
 * Dificultad: FÁCIL
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
for x in range(1,101): # Iteramos en "x" desde el 1 hasta el 101.
    if x % 3 == 0 and x % 5 == 0: # Comprobamos si son divisibles entre 3 y 5, y se imprime "FizzBuzz"
        print("FizzBuzz")
    elif x % 3 == 0: # Si son divisibles entre 3 se imprime "Fizz"
        print("Fizz")
    elif x % 5 == 0: # Si son divisibles entre 5 se imprime "Buzz"
        print("Buzz")
    else:
        print(x) # El resto de números que no entran en las anteriores condiciones se imprimen como numeros.