from django.db import models

# Create your models here.
class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.city} ({self.code})"

class Flight(models.Model):
	#ForeignKey to reference other models. (CASCADE) If airport key is deleted, also delete flight entry. Related name allows for finding flight from airport
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
	duration = models.IntegerField()

	#Create a function for returning nice string representation
	def __str__(self):
		return f"{self.id}: {self.origin} to {self.destination}"
