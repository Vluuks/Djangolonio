from django import forms
from .models import *

# class NewNPCForm(forms.ModelForm):
#     class Meta:
#         model = NPC
#         # without foreign keys for now
#         fields = ['name', 'age', 'gender', 'status']

class NewNPCForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    race = forms.ModelChoiceField(queryset=Race.objects.all())
    name = forms.CharField(label='Name', max_length=40)
    alignment = forms.ModelChoiceField(queryset=Alignment.objects.all())


