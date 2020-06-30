from django import forms
from .models import Set

class Fullset(forms.ModelForm):
        opts = (('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'))
        answer0=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer1=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer2=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer3=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer4=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer5=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer6=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer7=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer8=forms.CharField(label="Ans",widget=forms.Select(choices=opts))
        answer9=forms.CharField(label="Ans",widget=forms.Select(choices=opts))

        class Meta:
                model=Set
                exclude=['submitby']

