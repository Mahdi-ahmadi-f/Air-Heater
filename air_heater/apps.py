from django.apps import AppConfig




class AirHeaterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'air_heater'

    # def ready(self):
    #     from . import mqtt_subscriber, mqtt_publisher
    #     mqtt_subscriber.start_mqtt()
    #     mqtt_publisher.start_publisher()




