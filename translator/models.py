from django.db import models
from django.conf import settings
from django.urls import reverse

from martor.models import MartorField


class Project(models.Model):
    class Status(models.TextChoices):
        TRANSLATING = 'translating','Translating'
        TRANSLATED = 'translated', 'Translated'
        PENDING = 'pending', 'Pending'

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE,
                             related_name='owner')
    contributer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    related_name='contributer')
    status = models.CharField(max_length=15,
                              choices=Status.choices,
                              default='translating')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    source_github = models.URLField(max_length=200, unique=True)
    project_github = models.URLField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('translator:projects', args=[self.name])
    
    def __str__(self):
        return '{} created by {} '.format(self.name, self.owner)
    
class Text(models.Model):
    name = models.CharField(max_length=250)
    context = MartorField()
    slug = models.SlugField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.name
 
