# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def calcular_area(poligono):
    # Verificar el tipo de polígono y realizar el cálculo del área correspondiente

    if poligono['tipo'] == 'triangulo':  # Si el tipo de polígono es 'triangulo'
        area = (poligono['base'] * poligono['altura']) / 2  # Calcular el área del triángulo
        print(f"El área del triángulo es {area}")  # Mostrar el resultado del cálculo del área
        return area  # Devolver el valor del área calculada

    elif poligono['tipo'] == 'cuadrado':  # Si el tipo de polígono es 'cuadrado'
        area = poligono['lado'] * poligono['lado']  # Calcular el área del cuadrado
        print(f"El área del cuadrado es {area}")  # Mostrar el resultado del cálculo del área
        return area  # Devolver el valor del área calculada

    elif poligono['tipo'] == 'rectangulo':  # Si el tipo de polígono es 'rectangulo'
        area = poligono['base'] * poligono['altura']  # Calcular el área del rectángulo
        print(f"El área del rectángulo es {area}")  # Mostrar el resultado del cálculo del área
        return area  # Devolver el valor del área calculada

    else:
        # Si el tipo de polígono no es válido, se muestra un mensaje de error
        print("El tipo de polígono no es válido.")
        return None  # Devolver None en caso de polígono no válido


# Ejemplos de uso

triangulo = {'tipo': 'triangulo', 'base': 10.0, 'altura': 5.0}
calcular_area(triangulo)  # Calcula y muestra el área del triángulo

cuadrado = {'tipo': 'cuadrado', 'lado': 4.0}
calcular_area(cuadrado)  # Calcula y muestra el área del cuadrado

rectangulo = {'tipo': 'rectangulo', 'base': 5.0, 'altura': 7.0}
calcular_area(rectangulo)  # Calcula y muestra el área del rectángulo
