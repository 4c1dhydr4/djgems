from django.db import models

PROFILE_CHOICES = [
	('1','Clientes'),
	('2','Conductor'),
]

class Gem(models.Model):
	nombre = models.CharField(max_length=50)
	latitude = models.DecimalField(decimal_places=6, max_digits=8)
	longitude = models.DecimalField(decimal_places=6, max_digits=8)

	def __str__(self):
		return '{}'.format(self.nombre)

class GemProfile(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	photo = models.URLField()

	def __str__(self):
		return '{}'.format(self.username)


class Configuration(models.Model):
	factor = models.DecimalField(decimal_places=6, max_digits=8)
	left_right = models.BooleanField()
	simulation_active = models.BooleanField()

	def __str__(self):
		if self.simulation_active:
			active = 'Activo'
		else:
			active = 'No Activo'

		if self.left_right:
			direction = 'Derecha'
		else:
			direction = 'Izquierda'
		return 'Factor {} - {} - {}'.format(active, direction, self.factor)