from django import forms
from .models import Set

class Fullset(forms.ModelForm):

        class Meta:
                model=Set
                exclude=['submitby', 'marks_obtained']

