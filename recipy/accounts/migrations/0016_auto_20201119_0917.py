# Generated by Django 2.2.7 on 2020-11-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20201119_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='allergens',
            field=models.CharField(choices=[('', 'None'), ('1', 'Allergen 1'), ('2', 'Allergen 2'), ('3', 'Allergen 3'), ('4', 'Allergen 4'), ('5', 'Allergen 5')], max_length=10),
        ),
    ]
