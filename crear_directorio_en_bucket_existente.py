import boto3
import json

def lambda_handler(event, context):
    # Entrada (json)
    #body = json.loads(event['body'])
    nombre_bucket = event['body']['bucket_name']
    nombre_directorio = event['body']['directory_name'] + '/'

    # Proceso
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=nombre_bucket, Key=nombre_directorio)
        mensaje = f'Directorio "{nombre_directorio}" creado en el bucket "{nombre_bucket}".'
        status_code = 201
    except Exception as e:
        mensaje = f'Error al crear el directorio: {str(e)}'
        status_code = 400

    # Salida
    return {
        'statusCode': status_code,
        'message': mensaje
    }