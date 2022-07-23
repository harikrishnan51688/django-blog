import hashlib
import imp
from django.db import models
import uuid
from users.models import Profile
from django_resized import ResizedImageField
from ckeditor_uploader.fields import RichTextUploadingField
import readtime


# Create your models here.
class Article(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    heading = models.CharField(max_length=200)
    discription = models.CharField(max_length=300)
    category = models.CharField(max_length=100, null=True, blank=True)
    featured_image = ResizedImageField("Thumbnail Image",size=[1200,720], null=True, blank=True, default='images/blog_img/no-photo.jpg', upload_to='images/blog_img/')
    # text_field = models.TextField(null=True, blank=True)
    text_field =  RichTextUploadingField("Content",null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    comment_total = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.heading
    

    def get_readtime(self):
        try: 
            result = readtime.of_html(self.text_field)
            minutes = result.minutes
            return minutes
        except:
            return 1


    @property
    def getcommentcount(self):
        comments = self.comment_set.all()
        total_comment = comments.count()
        self.comment_total = total_comment
        self.save()


class Comment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)
    
    # @property
    def gravatar_url(self):
        # Get the md5 hash of the email address
        md5 = hashlib.md5(self.owner.email.encode())
        digest = md5.hexdigest()

        return 'http://www.gravatar.com/avatar/{}?s=80&d=retro&r=g'.format(digest)
        

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.name
