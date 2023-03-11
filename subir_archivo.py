import boto3
import datetime
from bs4 import BeautifulSoup

client = boto3.client('s3')


def subir_arhivo():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('descargararchivomitula')
    obj = bucket.Object(f"{datetime.datetime.now().strftime('%Y-%m-%d')}.html")
    body = obj.get()['Body'].read()
    soup = BeautifulSoup(body, 'html.parser')
    properties = soup.find_all('div', {'class': 'listing-card__information-main'})
    data = []

    for property in properties:
        price = property.find('div', {'class': 'listing-card__price-wrapper'}).text.strip()
        sqft = property.find_all('div', {'class': 'listing-card__property'})
        sqft2 = sqft
        casa = [price]
        for property2 in sqft2:
            casa.append(property2.text.strip())
        data.append(casa)
    print(data)
    s = ""
    s = s + " Precio, num_habitaciones, num_banos, metros_cuadrados\n"
    for fila in data:
        if len(fila) >= 4:
            s = s + fila[0] + "," + fila[1].replace(".", " ") + "," + fila[2].replace(".", " ") + "," + fila[3] + "\n"
        else:
            s = s + "\n"
    client = boto3.client('s3')
    client.put_object(Body=s, Bucket='descargararchivomitulafinal', Key=f"{datetime.datetime.now().strftime('%Y-%m-%d')}.csv")