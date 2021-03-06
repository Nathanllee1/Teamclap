from django import forms
from users.models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class EmailForm(forms.Form):
    subject = forms.CharField(required=True, label='subject', max_length=100)
    message = forms.CharField(required=True, label='message')
    recipients = forms.ModelChoiceField(queryset=CustomUser.objects.all())

