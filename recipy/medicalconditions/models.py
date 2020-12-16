from django.db import models

# Create your models here.

class MedicalConditions(models.Model):
    name = models.CharField(max_length=50)
    group = models.OneToMany(MedicalConditionsGroup, on_delete=models.CASCADE)


class MedicalConditionsGroup(models.Model):
    group = models.CharField(max_length=50)


