from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

from martor.models import MartorField




class Project(models.Model):
    class Status(models.TextChoices):
        TRANSLATING = 'translating','Translating'
        TRANSLATED = 'translated', 'Translated'
        PENDING = 'pending', 'Pending'

    class Access(models.TextChoices):
        PUBLIC = 'pu', 'Public'
        PRIVATE = 'pr', 'Private'

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE,
                             related_name='owner')
    assigned_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
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
    access = models.CharField(max_length=2,
                              choices=Access.choices,
                              default='pu')
    source_github = models.URLField(max_length=200, unique=True)
    project_github = models.URLField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('translator:project_detail', args=[self.slug])
    
    def assigned_owner(self, user):
        self.assigned_owner = user
        self.save()
    
    def translated(self):
        self.status = Project.Status.TRANSLATED
        self.save()

    def pending(self):
        self.status = Project.Status.PENDING
        self.save()
    
    def is_public(self):
        if self.access == 'pu':
            return True
        return False

class Text(models.Model):
    name = models.CharField(max_length=250)
    context = MartorField()
    slug = models.SlugField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="text")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('translator:text_detail', args=[self.project.slug, self.slug])
 
