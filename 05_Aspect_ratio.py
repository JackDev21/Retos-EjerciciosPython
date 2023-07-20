# Crea un programa que se encargue de calcular el aspect ratio de una
# imagen a partir de una url.
# - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
# - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#   imagen de 1920#1080px.
#


from PIL import Image  # Importamos la clase Image de la biblioteca PIL para trabajar con imágenes
import requests  # Importamos la biblioteca requests para realizar solicitudes HTTP
import math  # Importamos la biblioteca math para realizar cálculos matemáticos
from io import BytesIO  # Importamos la clase BytesIO para trabajar con contenido binario en memoria

def obtener_aspect_ratio(url_imagen):
    try:
        response = requests.get(url_imagen)  # Realizamos una solicitud GET a la URL para obtener el contenido de la imagen
        imagen = Image.open(BytesIO(response.content))  # Abrimos la imagen utilizando la clase Image y el contenido obtenido
        ancho, alto = imagen.size  # Obtenemos el ancho y alto de la imagen
        mcd = math.gcd(ancho, alto)  # Calculamos el máximo común divisor entre el ancho y alto utilizando la función gcd de la biblioteca math
        aspect_ratio = f"{ancho // mcd}:{alto // mcd}"  # Calculamos el Aspect Ratio dividiendo el ancho y alto por el máximo común divisor
        print(f"El Aspect Ratio es: {aspect_ratio}")  # Mostramos el resultado del Aspect Ratio utilizando la función print()
    except Exception:
        print("La URL proporcionada no es una imagen válida.")

# Ejemplo de uso
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
obtener_aspect_ratio(url)



