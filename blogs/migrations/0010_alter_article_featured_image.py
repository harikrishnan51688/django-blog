# Generated by Django 4.0.1 on 2022-02-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_alter_article_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=models.ImageField(blank=True, default='images/0f53970e02.jpg', null=True, upload_to='images/'),
        ),
    ]
