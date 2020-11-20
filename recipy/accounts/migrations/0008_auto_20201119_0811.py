# Generated by Django 2.2.7 on 2020-11-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=6),
        ),
    ]
