from django import forms
from . models import movie

class movieupdate(forms.ModelForm):
    class Meta:
        model=movie
        fields=['Name','desc','year','Image']

