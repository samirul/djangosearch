from django.forms import ModelForm
from .models import phoneName


class PhoneImage(ModelForm):
    class Meta:
        model = phoneName
        fields = ['avatar']