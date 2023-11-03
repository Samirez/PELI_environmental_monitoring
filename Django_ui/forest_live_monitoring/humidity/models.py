from django.db import models

class sensors(models.Model):
    Node_id = models.AutoField(primary_key=True)
    Latitude = models.DecimalField(max_digits=8, decimal_places=6)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        db_table = 'sensors'
        unique_together = (('Latitude', 'Longitude'),)

class sensorReadings(models.Model):
    ID = models.AutoField(primary_key=True)
    Node_id = models.ForeignKey(sensors, on_delete=models.CASCADE)
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sensorReadings'

