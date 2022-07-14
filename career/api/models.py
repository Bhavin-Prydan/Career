from django.db import models

# Create your models here.
class Candidate(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=200)
	Email = models.EmailField()
	PhoneNumber = models.BigIntegerField()
	Country = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	City = models.CharField(max_length=50)
	Current_Organization = models.CharField(max_length=350)
	Total_Experience = models.CharField(max_length=100)
	Relavant_Experience = models.CharField(max_length=100)
	Joining_Period = models.CharField(max_length=100)
	Current_AnnualPay = models.CharField(max_length=100)
	Expected_AnnualPay = models.CharField(max_length=100)
	Position_AppliedFor = models.CharField(max_length=100)
	Personal_Website = models.TextField()
	LinkedIn_Profile = models.TextField()
	Twitter_Url = models.TextField()
	Resume = models.FileField(upload_to ='Documents')
	Discription = models.TextField()

	def __str__(self):
		return Name
