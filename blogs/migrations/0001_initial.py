# Generated by Django 4.0.5 on 2022-08-31 05:52

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('heading', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=300)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('featured_image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/blog_img/no-photo.jpg', force_format='JPEG', keep_meta=True, null=True, quality=-1, scale=None, size=[1200, 720], upload_to='images/blog_img/', verbose_name='Thumbnail Image')),
                ('text_field', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content')),
                ('comment_total', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('text', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.article')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blogs.tag'),
        ),
    ]
