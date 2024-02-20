from django import forms
from django.forms import ModelForm
from hadsdb.models import Dane

class DatabaseQueryForm(forms.Form):
    pass

class QueryHadsForm(ModelForm):
    class Meta:
        model = Dane
        fields = ['mass', 'feh', 'fov']

