from django.db import models


class FoodPreparationTypeCategory(models.Model):

    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Food Preparation Type Category'
        verbose_name_plural = 'Food Preparation Type Categories'

    def __str__(self):
        return self.name


class FoodpreparationType(models.Model):

  name = models.CharField(max_length=120)
  description = models.TextField(max_length=1024, default=None, blank=True)
  category = models.ForeignKey(FoodPreparationTypeCategory, on_delete=models.CASCADE, default=None)

  class Meta:
    verbose_name = 'Food Preparation Type'
    verbose_name_plural = 'Food Preparation Types'

  def __str__(self):
    return self.name
