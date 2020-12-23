from django.db import models


class MedicalConditionsGroup(models.Model):
    group = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = 'Medical Condition Group'
        verbose_name_plural = 'Medical Condition Groups'

    def __str__(self):
        return self.group


class MedicalConditions(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(MedicalConditionsGroup, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medical Condition'
        verbose_name_plural = 'Medical Conditions'

    def __str__(self):
        return self.name

