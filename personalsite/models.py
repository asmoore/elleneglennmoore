from django.db import models
import os
from django import forms

def get_image_path(instance, filename):
    return os.path.join('src/img/', filename)

class Biography(models.Model):
    text = models.TextField()

class Event(models.Model):
    event_date = models.TextField()
    event_description = models.TextField()

class Media(models.Model):
    media_text = models.TextField()
    media_description = models.TextField()
    VIDEO = 'VI'
    TEXT = 'TX'
    IMAGE = 'IM'
    MEDIA_TYPE = (
        (VIDEO, 'Video'),
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
    )
    media_type = models.CharField(max_length=2,
                                      choices=MEDIA_TYPE,
                                      default=VIDEO)
