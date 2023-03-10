from urllib.request import urlopen
import boto3
from bs4 import BeautifulSoup
def lambda_handler(event, context):
    # TODO implement
    url = "https://casas.mitula.com.co/searchRE/nivel3-Chapinero/nivel2-Bogot%C3%A1/nivel1-Cundinamarca/q-Bogot%C3%A1-Chapinero"
    with urlopen(url) as response:
        body = response.read()
    client = boto3.client("s3")
    client.put_object(Body=body,Bucket="s3://landing-casas-xxx/yyyy-mm-dd.html",Key="dolar_timestamp.txt")