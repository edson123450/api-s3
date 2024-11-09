import boto3
import json

def lambda_handler(event, context):
    # Entrada (json)
    #body = json.loads(event['body'])
    nombre_bucket = event['body']['bucket_name']

    # Proceso
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(Bucket=nombre_bucket)
        mensaje = f'Bucket "{nombre_bucket}" creado exitosamente.'
        status_code = 201
    except Exception as e:
        mensaje = f'Error al crear el bucket: {str(e)}'
        status_code = 400

    # Salida
    return {
        'statusCode': status_code,
        'message': mensaje
    }