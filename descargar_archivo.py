import boto3
import requests
import datetime

client = boto3.client('s3')
BUCKET_NAME = 'descargararchivomitula'


def descargar_html():
    url = 'https://casas.mitula.com.co/searchRE/nivel2-Bogot%C3%A1/nivel1-Cundinamarca/op-1/tipo-Casa/q-Bogot%C3%A1'
    response = requests.get(url)
    html_file = "{}.html".format(datetime.datetime.now().strftime('%Y-%m-%d'))
    client.put_object(Bucket=BUCKET_NAME, Key=html_file, Body=response.content)