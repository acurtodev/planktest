from django.db import models


class Satellite(models.Model):
    name = models.CharField(max_length=140, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"""name: {self.name}, lat: {self.latitude}, lon: {self.longitude}"""

    def to_json(self):
        return {
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
