from django.forms import ModelForm
from .models import State


class StateDetailsForm(ModelForm):
    class Meta:
        model = State
        fields = '__all__'
