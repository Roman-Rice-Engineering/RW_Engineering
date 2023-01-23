from django.db import models
from django.utils import timezone

class Project(models.Model):
    
    start_time = models.DateTimeField(default = timezone.now)
    end_time = models.DateTimeField(null = True, blank = True)

    version_release = models.IntegerField(default = 0)
    version_patch = models.IntegerField(default = 0)
    version_feature = models.IntegerField(default = 0)

    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 1000)
    thumbnail = models.ImageField(null = True, blank = True, upload_to = "projects/")
    
