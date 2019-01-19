from django.db import models

class Profile(models.Model):
	image = models.ImageField(upload_to='images/')
	desc = models.CharField(max_length=200)

	def __str__(self):
		return self.desc[:20]
		