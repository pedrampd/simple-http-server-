from django import forms

class TextForm(forms.Form):
    jtext = forms.JSONField()
