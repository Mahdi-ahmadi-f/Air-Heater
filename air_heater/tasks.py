from celery import shared_task
from opcua import Client
from .models import Temperature
import redis
from django.utils import timezone



@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5)
def fetch_temperature_task(self):
    url = "opc.tcp://100.65.57.80:49580"
    client = Client(url)

    try:
        client.connect()

        node_id = "ns=2;s=Data.Temperature"
        temp_node = client.get_node(node_id)
        raw_value = temp_node.get_value()
        if raw_value is None:
            raise ValueError("No value received from OPC UA")
        value = round(float(raw_value), 1)


        Temperature.objects.create(value=value)


        r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
        r.set("latest_temperature", value)
        r.set("latest_temperature_ts", timezone.now().isoformat())

        print(f"Saved Temperature: {value}")

    finally:
        client.disconnect()