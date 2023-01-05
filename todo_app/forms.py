from . models import task
from . import views
from django import forms


class todoforms(forms.ModelForm):
    class Meta:
        model=task #model name and fields
        fields=['name','age','priority','email','date']
