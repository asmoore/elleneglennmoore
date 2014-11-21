import os
from django.db import models
from django.core.files.storage import FileSystemStorage

class Post(models.Model):
    HIDDEN = 1
    DRAFT = 2
    PUBLISHED = 3

    STATUS_CHOICES  = (
        (HIDDEN, 'Hidden'),
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    content = models.TextField()
    status = models.SmallIntegerField(default=DRAFT, choices=STATUS_CHOICES)
    featured = models.BooleanField(default=False)
    comments = models.BooleanField(default=True)
    created = models.DateTimeField()
    video_link = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/', blank=True)

    class Meta:
        ordering = ['featured', '-created']

    def __unicode__(self):
        return u'%s' % self.pk

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post', (), {
        'year' : self.created.year,
        'month' : self.created.strftime("%m"),
        'slug' : self.slug
    })