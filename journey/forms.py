from django import forms
from django.forms.models import inlineformset_factory
from .models import Journey, Place


class JourneyForm(forms.ModelForm):

    class Meta:
        model = Journey
        fields = ('location', 'cost')


PlaceFormSet = inlineformset_factory(
    Journey,
    Place,
    fields=['name', 'link'],
    extra=2,
    can_delete=True
)
