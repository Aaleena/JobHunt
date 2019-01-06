from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=500)
	detail = models.TextField()
	category_choices = (
		('IT','IT'),
		('teaching','Teaching'),
		('banking','Banking'),
		('marketing','Marketing'),
	)
	category=models.CharField(max_length=20,choices=category_choices,default='IT',)
	salary = models.IntegerField()
	def __str__(self):
		return self.title
