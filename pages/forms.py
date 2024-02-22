from django import forms
from django.forms import ModelForm
from hadsdb.models import Dane
from django.utils.safestring import mark_safe

class DatabaseQueryForm(forms.Form):
    pass

class QueryHadsForm(ModelForm):
    class Meta:
        model = Dane
        fields = ['mass', 'feh', 'fov']
        labels = {
            "feh": "[Fe/H]",
            "fov": mark_safe("f<sub>ov</sub>")
        }

