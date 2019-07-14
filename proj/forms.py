from django.forms import ModelForm, TextInput
from .models import IP

class IPForm(ModelForm):
    class Meta:
        model = IP
        fields = ['ipaddress']
        widgets = {'ipaddress' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter IP address'})}