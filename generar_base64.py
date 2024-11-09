import base64

ruta_imagen = "/lambdas/api-s3/galleta01-small.png"

# Leer la imagen en modo binario y convertir a Base64
with open(ruta_imagen, "rb") as imagen_file:
    imagen_base64 = base64.b64encode(imagen_file.read()).decode('utf-8')

# Imprimir el resultado
print(imagen_base64)