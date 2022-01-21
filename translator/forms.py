from django import forms

from translator.models import Project, Text


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'is_public', 'source_github', 'project_github')

class TextForm(forms.ModelForm):

    class Meta:
        model = Text
        fields = ('name', 'context')