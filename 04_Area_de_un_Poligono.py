# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def calcular_area(poligono):
    # Definimos una función llamada calcular_area que toma un parámetro llamado poligono.

    # Calcula y retorna el área de un polígono.
    # Los polígonos soportados son Triángulo, Cuadrado y Rectángulo.

    if type(poligono) == tuple and len(poligono) >= 2:
        # Verificamos si el parámetro poligono es una tupla y si tiene al menos dos elementos.
        
        tipo_poligono = poligono[0]
        # Asignamos el primer elemento de la tupla a la variable tipo_poligono.
        
        medidas = poligono[1:]
        # Las medidas del polígono se encuentran en los demás elementos de la tupla.
        
        if tipo_poligono == "Triangulo" and len(medidas) == 2:
            # Si el tipo de polígono es "Triangulo" y tiene exactamente dos medidas,
            
            base, altura = medidas
            # asignamos las medidas a las variables base y altura.
            
            area = (base * altura) / 2
            # Calculamos el área del triángulo utilizando la fórmula correspondiente.
            
            print(f"El área del triángulo es: {area}")
            # Imprimimos el resultado del cálculo del área del triángulo.
            
            return area
            # Retornamos el valor del área calculada.
        
        elif tipo_poligono == "Cuadrado" and len(medidas) == 1:
            # Si el tipo de polígono es "Cuadrado" y tiene exactamente una medida,
            
            lado = medidas[0]
            # asignamos la medida a la variable lado.
            
            area = lado ** 2
            # Calculamos el área del cuadrado utilizando la fórmula correspondiente.
            
            print(f"El área del cuadrado es: {area}")
            # Imprimimos el resultado del cálculo del área del cuadrado.
            
            return area
            # Retornamos el valor del área calculada.
        
        elif tipo_poligono == "Rectangulo" and len(medidas) == 2:
            # Si el tipo de polígono es "Rectangulo" y tiene exactamente dos medidas,
            
            base, altura = medidas
            # asignamos las medidas a las variables base y altura.
            
            area = base * altura
            # Calculamos el área del rectángulo utilizando la fórmula correspondiente.
            
            print(f"El área del rectángulo es: {area}")
            # Imprimimos el resultado del cálculo del área del rectángulo.
            
            return area
            # Retornamos el valor del área calculada.
        
        else:
            # Si el tipo de polígono no es ninguno de los soportados o si las medidas no son correctas,
            
            print("Error: Polígono no soportado")
            # Imprimimos un mensaje de error indicando que el polígono no es soportado.
            
            return None
            # Retornamos None para indicar que no se pudo calcular el área.
    
    else:
        # Si el parámetro poligono no es una tupla o no tiene al menos dos elementos,
        
        print("Error: Debe ingresar un polígono como tupla con al menos dos elementos")
        # Imprimimos un mensaje de error indicando que se debe ingresar un polígono válido.
        
        return None
        # Retornamos None para indicar que no se pudo calcular el área.

# Ejemplo de uso de la función calcular_area()

triangulo = ("Triangulo", 5, 10)
cuadrado = ("Cuadrado", 7)
rectangulo = ("Rectangulo", 3, 8)

calcular_area(triangulo)   # Salida: El área del triángulo es: 25.0
calcular_area(cuadrado)    # Salida: El área del cuadrado es: 49
calcular_area(rectangulo)  # Salida: El área del rectángulo es: 24
