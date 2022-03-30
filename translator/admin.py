from django.contrib import admin
from django.db import models

from martor.widgets import AdminMartorWidget

from translator.models import Text,Project

@admin.register(Text)
class TextModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    list_display = ('name', 'context', 'slug', 'project', 'created')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
                      




@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'owner', 'contributer', 'status', 
                    'description', 'created', 'access', 'source_github', 'project_github')
    list_filter = ('owner', 'status', 'created', 'access')
    search_fields = ('name', 'source_github', 'project_github')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ('status', 'created')                    