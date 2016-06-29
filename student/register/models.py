from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.firstname+'-'+self.lastname+'-'+self.username
