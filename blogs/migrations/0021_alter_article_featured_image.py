# Generated by Django 4.0.1 on 2022-06-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_alter_article_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=models.ImageField(blank=True, default='images/no-photo.jpg', null=True, upload_to='images/'),
        ),
    ]
