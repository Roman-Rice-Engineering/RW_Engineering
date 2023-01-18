from django.db import models
from django.utils import timezone

class WeeklyBlogPost(models.Model):
    title = models.CharField(max_length = 200)
    thumbnail = models.ImageField(upload_to = 'static/blog')
    creation_time = models.DateTimeField(default = timezone.now)

class Content(models.Model):
    blog = models.ForeignKey(WeeklyBlogPost, on_delete = models.CASCADE)
    content_type = models.CharField(max_length = 10)

#Content types
class Text(models.Model):
    content_container = models.ForeignKey(Content, on_delete = models.CASCADE)
    text = models.CharField(max_length = 500)

class Code_S(models.Model):
    content_container = models.ForeignKey(Content, on_delete = models.CASCADE)
    code = models.CharField(max_length = 4000)
    
class Code_M(models.Model):
    content_container = models.ForeignKey(Content, on_delete = models.CASCADE)
    code = models.CharField(max_length = 20000)

class Code_L(models.Model):
    content_container = models.ForeignKey(Content, on_delete = models.CASCADE)
    code = models.CharField(max_length = 100000)

class Image(models.Model):
    content_container = models.ForeignKey(Content, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'static/blog')
    image_description = models.CharField(max_length = 200)