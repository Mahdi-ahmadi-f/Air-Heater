from django.db import models




class Temperature(models.Model):
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.value} °C at {self.created_at}"



