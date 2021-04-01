from django import forms


class InputForm(forms.Form):
    name = forms.CharField()
