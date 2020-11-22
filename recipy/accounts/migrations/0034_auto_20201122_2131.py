# Generated by Django 2.2.7 on 2020-11-22 21:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20201122_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='medical_conditions',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Group 1', (('aids', 'AIDS'), ('hearth-health', 'Hearth Health'), ('kidney-disease', 'Kidney Disease'))), ('Group 2', (('diabetes', 'Diabetes'), ('cancer', 'Cancer'), ('lupus', 'Lupus')))], max_length=240, verbose_name='medical_conditions'),
        ),
    ]
