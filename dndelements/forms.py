from django import forms
from .models import NPC

class NewNPCForm(forms.ModelForm):
    class Meta:
        model = NPC
        # without foreign keys for now
        fields = ['name', 'age', 'gender', 'status']