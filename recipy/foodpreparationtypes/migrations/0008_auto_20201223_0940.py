# Generated by Django 2.2.7 on 2020-12-23 09:40

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('foodpreparationtypes', '0007_auto_20201223_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodpreparationtype',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='foodpreparationtypes.Foodpreparationtype'),
        ),
    ]
