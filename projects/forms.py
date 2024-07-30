from django.forms import ModelForm
# Django forms
from django import forms
from . import models

class ProjectForm(ModelForm):    
    class Meta:
        model = models.Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        # widgets to style the form
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Title'})

        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Description'})