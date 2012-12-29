from django.db import models

# Create your models here.
class Name(models.Model):
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=10) #male, female, both
	origin = models.CharField(max_length=20,blank=True, default="")
	meaning = models.TextField(blank=True, default="")
	favorite = models.BooleanField(default=False, blank=True)

class NameUsage(models.Model):
	title = models.CharField(max_length=200)
	name = models.ForeignKey(Name)