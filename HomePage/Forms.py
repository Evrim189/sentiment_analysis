from django import forms

class NameForm(forms.Form):
    Text = forms.CharField(label='Kelime/Cümle', max_length=100)
