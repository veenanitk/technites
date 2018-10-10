from django.db import models

class paste(models.Model):
    image = ImageField(max_length=1000000)
	
		