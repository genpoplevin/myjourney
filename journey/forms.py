from django import forms
from .models import Journey


class JourneyForm(forms.ModelForm):

    class Meta:
        model = Journey
        fields = ('location', 'cost', 'heritage')
