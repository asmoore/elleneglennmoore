import os

from django.db import models
from django import forms

def get_image_path(instance, filename):
    return os.path.join('src/img/', filename)

class Biography(models.Model):
    text = models.TextField()

class Event(models.Model):
    event_title = models.TextField()
    event_description = models.TextField()
    event_date = models.DateTimeField()


class Work(models.Model):
    work_text = models.TextField()
    POETRY = 'PO'
    PROJECTS = 'PR'
    OTHER = 'OT'
    WORK_TYPE = (
        (POETRY, 'Poetry publications'),
        (PROJECTS, 'Projects and collaborations'),
        (OTHER, 'Additional publications'),
    )
    work_type = models.CharField(max_length=2,
                                      choices=WORK_TYPE,
                                      default=POETRY)

