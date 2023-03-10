import json
import boto3
from datetime import datetime
import csv
def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("dolar-raw-initial")
    obj = bucket.Object("dolar_timestamp.txt")
    body = obj.get()["Body"].read()
    s=''
    m=json.loads(body)
    print(m)
    for fila in m:
        fecha=datetime.fromtimestamp(int(fila[0])/1000)
        dato=fila[1]
        fecha=str(fecha)
        s=s+fecha+","+dato+"\n"
        #FechaDescarga, Barrio, Valor, NumHabitaciones, NumBanos, mts2

client = boto3.client("s3")
client.put_object(Body=s,Bucket="finaldolar",Key="s3://casas-final-xxx/yyyy-mm-dd.csv")
