from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from multiselectfield import MultiSelectField

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,
        primary_key=True,)

    birthdate = models.DateField(null=True, blank=True)

    UNITS_OPTIONS = (
        ('1','Imperial'),
        ('2','Metric'),
    )
    units = models.CharField(max_length=1, choices=UNITS_OPTIONS, default='EU' )

    SEX_OPTIONS = (
        ('M','Male'),
        ('F','Female'),
    )
    sex = models.CharField(max_length=7, choices=SEX_OPTIONS, default='F' )

    height =models.PositiveSmallIntegerField(default=0)

    weight = models.PositiveSmallIntegerField(default=0)

    MEALS_PER_DAY_OPTIONS = (
        ('1','1 meal'),
        ('2','2 meals'),
        ('3','3 meals'),
        ('4','4 meals'),
        ('5','5 meals'),
    )
    meals_per_day = models.CharField(max_length=1, choices=MEALS_PER_DAY_OPTIONS, default='3')

    ALLERGENS_OPTIONS = (
        ('allergen-1','Allergen 1'),
        ('allergen-2','Allergen 2'),
        ('allergen-3','Allergen 3'),
        ('allergen-4','Allergen 4'),
        ('allergen-5','Allergen 5'),
    )
    allergens = MultiSelectField(max_length=120, choices=ALLERGENS_OPTIONS, blank=True, verbose_name="allergens")

    # MEDICAL_CONDITIONS_OPTIONS = (
    #     ('aids','AIDS'),
    #     ('hearth-health','Hearth Health'),
    #     ('kidney-disease','Kidney Disease'),
    #     ('diabetes','Diabetes'),
    #     ('cancer','Cancer'),
    #     ('lupus','Lupus'),
    # )

    MEDICAL_CONDITIONS_OPTIONS = (
        ('Group 1',(
            (1,'AIDS'),
            (2,'Hearth Health'),
            (3,'Kidney Disease')
          )
        ),

        ('Group 2',(
            (4,'Diabetes'),
            (5,'Cancer'),
            (6,'Lupus')
          )
        )
    )

    medical_conditions = MultiSelectField(max_length=240, choices=MEDICAL_CONDITIONS_OPTIONS, blank=True, verbose_name="medical_conditions")

    RISK_FACTORS_OPTIONS = (
        ('weight-loss-within-3-months','Weight loss within 3 months'),
        ('reduced-dietary-intake-in-the-last-week','Reduced dietary intake in the last week'),
        ('icu-patient','ICU patient'),
    )
    risk_factors = MultiSelectField(max_length=120, choices=RISK_FACTORS_OPTIONS, blank=True, verbose_name="risk_factors")



    def __str__(self):
        return str(self.user)



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)