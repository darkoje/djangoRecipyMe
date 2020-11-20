from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from multiselectfield import MultiSelectField

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,
        primary_key=True,)

    birthdate = models.DateField(null=True)

    METRICS_OPTIONS = (
        ('US','USA'),
        ('EU','EU'),
        ('UK','UK'),
    )
    metrics = models.CharField(max_length=3, choices=METRICS_OPTIONS, default='EU' )

    SEX_OPTIONS = (
        ('M','MALE'),
        ('F','FEMALE'),
    )
    sex = models.CharField(max_length=7, choices=SEX_OPTIONS, default='F' )

    height =models.PositiveSmallIntegerField(default=0)

    weight = models.PositiveSmallIntegerField(default=0)

    MEALS_PER_DAY_OPTIONS = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    meals_per_day = models.CharField(max_length=1, choices=MEALS_PER_DAY_OPTIONS, default='3')

    ALLERGENS_OPTIONS = (
        ('allergen-1','Allergen 1'),
        ('allergen-2','Allergen 2'),
        ('allergen-3','Allergen 3'),
        ('allergen-4','Allergen 4'),
        ('allergen-5','Allergen 5'),
    )
    #allergens = models.CharField(max_length=10, choices=ALLERGENS_OPTIONS)
    allergens = MultiSelectField(max_length=100, choices=ALLERGENS_OPTIONS, blank=True)

    MEDICAL_CONDITIONS_OPTIONS = (
        ('1','AIDS'),
        ('2','Hearth Health'),
        ('3','Kidney Disease'),
        ('4','Diabetes'),
        ('5','Cancer'),
        ('6','Lupus'),
    )
    medical_conditions = MultiSelectField(max_length=14, choices=MEDICAL_CONDITIONS_OPTIONS, blank=True)

    RISK_FACTORS_OPTIONS = (
        ('1','Weight loss within 3 months'),
        ('2','Reduced dietary intake in the last week'),
        ('3','ICU patient'),
    )
    risk_factors = MultiSelectField(max_length=14, choices=RISK_FACTORS_OPTIONS, blank=True)



    def __str__(self):
        return str(self.user)



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)