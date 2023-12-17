
from django import forms
from . models import Movie1
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie1
        fields=['name','desc','year','img']
        
    