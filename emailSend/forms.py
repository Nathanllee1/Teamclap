from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(label='body', max_length=500)