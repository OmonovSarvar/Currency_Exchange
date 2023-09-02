from django.forms import ModelForm, TextInput, NumberInput

from exchanger.models import Exchanger


class Widget(ModelForm):
    class Meta:
        model = Exchanger
        fields = ['value1', 'value2', 'value']

