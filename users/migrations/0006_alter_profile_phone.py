# Generated by Django 4.0.5 on 2022-07-22 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]