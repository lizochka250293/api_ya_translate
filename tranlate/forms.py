from django import forms
from django.forms.utils import ErrorList


class LangForm(forms.Form):
    word = forms.CharField(label='Слово')
    langs = forms.TypedChoiceField(label='язык')
    # langs = forms.ChoiceField()


