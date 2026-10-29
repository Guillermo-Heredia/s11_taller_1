import boto3
import os

def lambda_handler(event, context):
    try:
        nombre_bucket = event['body']['bucket']
        s3 = boto3.client('s3')
        
        region = boto3.session.Session().region_name or 'us-east-1'
        if region == 'us-east-1':
            s3.create_bucket(Bucket=nombre_bucket)
        else:
            s3.create_bucket(
                Bucket=nombre_bucket,
                CreateBucketConfiguration={'LocationConstraint': region}
            )

        return {
            'statusCode': 200,
            'mensaje': f'Bucket "{nombre_bucket}" creado exitosamente'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }