from django import forms

from martor.fields import MartorFormField

from translator.models import Project, Text


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'access', 'source_github', 'project_github')
        widgets = {
            'access': forms.RadioSelect,
            'description': forms.Textarea

        }

class TextForm(forms.ModelForm):

    context = MartorFormField()
    
    class Meta:
        model = Text
        fields = ('name', 'context')

class EditTextForm(forms.ModelForm):

    class Meta:
        model = Text
        fields = ['name', 'context']

class EditProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'access', 'source_github', 'project_github')
        widgets = {
            'access': forms.RadioSelect,
            'description': forms.Textarea

        }


