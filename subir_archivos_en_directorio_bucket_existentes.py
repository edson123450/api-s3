import boto3
import base64
import json

def lambda_handler(event, context):
    # Entrada (json)
    #body = json.loads(event['body'])
    nombre_bucket = event['body']['bucket_name']
    nombre_directorio = event['body']['directory_name']
    archivo_nombre = event['body']['file_name']
    archivo_base64 = event['body']['file_base64']

    # Decodificar Base64
    try:
        archivo_bytes = base64.b64decode(archivo_base64)
    except Exception as e:
        return {
            'statusCode': 400,
            'message': f'Error al decodificar Base64: {str(e)}'
        }

    # Proceso
    s3 = boto3.client('s3')
    ruta_completa = f"{nombre_directorio}/{archivo_nombre}"
    try:
        s3.put_object(Bucket=nombre_bucket, Key=ruta_completa, Body=archivo_bytes)
        mensaje = f'Archivo "{archivo_nombre}" subido al directorio "{nombre_directorio}" en el bucket "{nombre_bucket}".'
        status_code = 201
    except Exception as e:
        mensaje = f'Error al subir el archivo: {str(e)}'
        status_code = 400

    # Salida
    return {
        'statusCode': status_code,
        'message': mensaje
    }