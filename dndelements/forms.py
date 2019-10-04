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
    status = forms.CharField(label='Status', max_length=40)
    gender = forms.CharField(label='Gender', max_length=40)
    age = forms.IntegerField(label='age')
    alignment = forms.ModelChoiceField(queryset=Alignment.objects.all())


class NewCharacterForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(label='Name', max_length=40)
    race = forms.ModelChoiceField(queryset=Race.objects.all())
    player_class = forms.ModelChoiceField(queryset=PlayerClass.objects.all())
    gender = forms.CharField(label='Gender', max_length=40)
    age = forms.IntegerField(label='age')
    alignment = forms.ModelChoiceField(queryset=Alignment.objects.all())