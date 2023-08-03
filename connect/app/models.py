from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class job(models.Model):
	job_title = models.CharField(max_length=150)
	type = models.CharField(max_length=150)
	description =models.CharField(max_length=400)
	date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='images/')
	

	def __str__(self):
		return self.job_title
	

class Applicants(models.Model):
	Name = models.CharField(max_length=100)
	ssc = models.IntegerField(null=True)
	Hsc =models.IntegerField(null=True)
	Postgrad_cgpa = models.IntegerField()
	Resume = models.FileField()
