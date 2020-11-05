from django import forms
from .models import Room, Maid
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

class roomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields =('num', 'room_type')

class maidForm(forms.ModelForm):
    class Meta:
        model = Maid
        fields =('first_name', 'last_name', 'id_num')

class roomListForm(forms.ModelForm):
    class Meta:
        model = Room
        fields =('check_out', 'room_clean')
