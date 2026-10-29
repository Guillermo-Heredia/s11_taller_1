import boto3

def lambda_handler(event, context):
    try:
        nombre_bucket = event['body']['bucket']
        directorio = event['body']['directorio']
        
        # En S3 un directorio es un objeto cuya clave termina en '/'
        if not directorio.endswith('/'):
            directorio += '/'

        s3 = boto3.client('s3')
        s3.put_object(Bucket=nombre_bucket, Key=directorio)

        return {
            'statusCode': 200,
            'mensaje': f'Directorio "{directorio}" creado en el bucket "{nombre_bucket}"'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }