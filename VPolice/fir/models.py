from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
Gender = (
	('MALE','MALE'),
	('FEMALE','FEMALE'),
	)
face_types = (
	('Round','Round'),
	('Injury Mark','Injury Mark'),
	('Oval','Oval'),
	('Small Pox','Small Pox'),
	('Wrinkled','Wrinkled'),
	('Forhead-Broad','Forhead-Broad'),
	('Forhead-Narrow','Forhead-Narrow'),
	)
hair_types = (
	('Black','Black'),
	('Brown','Brown'),
	('White','White'),
	)
eye_types =(
	('Black','Black'),
	('Brown','Brown'),
	('Blue','Blue'),
	)
states = (
	('Haryana','Haryana'),
	('Rajasthan','Rajasthan'),
	('Hyderabad','Hyderabad'),
	('Delhi','Delhi'),
	)
vehicle = (
	('Car','Car'),
	('Truck','Truck'),
	('Bike','Bike'),
	('Scooter','Scooter'),
	)
class MissingChildren(models.Model):
	child_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	height = models.IntegerField()
	sex = models.CharField(max_length=100,choices = Gender,default='MALE')
	complexion = models.CharField(max_length=100)
	face = models.CharField(max_length=100,choices = face_types,default='Round')
	hair = models.CharField(max_length=100,choices = hair_types,default='Black')
	eye = models.CharField(max_length=100,choices = eye_types,default='Black')
	state = models.CharField(max_length=100,choices = states,default='Haryana')
	missing_date = models.DateField(null=True)

	def __str__(self):
		return '%s %s %s' %(self.child_id,self.name,self.age)

class StolenVehicles(models.Model):
	vehicle_id = models.AutoField(primary_key=True)
	vehicle_type = models.CharField(max_length=200, choices=vehicle,default='Car') 
	reg_num = models.CharField(max_length=200)
	eng_num = models.CharField(max_length=200)
	chassis_num = models.CharField(max_length=200)