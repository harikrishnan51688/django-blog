# Generated by Django 4.0.1 on 2022-06-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0022_comment_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
