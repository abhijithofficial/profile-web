from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateField(default=1)
	image = models.ImageField(upload_to='blog/')
	content = models.TextField()

	def __str__(self):
		return self.title
		
