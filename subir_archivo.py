import boto3
import base64

def lambda_handler(event, context):
    try:
        nombre_bucket = event['body']['bucket']
        directorio = event['body'].get('directorio', '').strip()
        nombre_archivo = event['body']['nombre_archivo']
        contenido = event['body']['contenido']

        # Normalizar la ruta del directorio
        if directorio and not directorio.endswith('/'):
            directorio += '/'

        key = f"{directorio}{nombre_archivo}"

        # Soportar texto plano o contenido codificado en Base64
        if event['body'].get('is_base64', False):
            body_bytes = base64.b64decode(contenido)
        else:
            body_bytes = contenido.encode('utf-8')

        s3 = boto3.client('s3')
        s3.put_object(Bucket=nombre_bucket, Key=key, Body=body_bytes)

        return {
            'statusCode': 200,
            'mensaje': f'Archivo "{nombre_archivo}" subido con éxito en la ruta "{key}"'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }