from django.db import models

# Create your models here.

class Employee(models.Model):

	empName = models.CharField(max_length=50)
	empRSA_ID = models.CharField(max_length=13)
	empLName = models.CharField(max_length=50)
	empDOB = models.DateField()
	empPos = models.CharField(max_length=25)
	empHireDt = models.DateField()
	employmentStatus = models.CharField(max_length=10)#part-time/permanent/contract

	def __str__(self):
		return self.empLName