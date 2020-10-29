from django import forms
from .models import Room
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

class Form(forms.ModelForm):
    class Meta:
        model = Room
        fields =('num', 'room_type', 'check_out',)