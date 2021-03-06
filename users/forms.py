from django.forms import ModelForm
from .models import Bio
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class BioForm(ModelForm):
    class Meta:
        model = Bio
        fields = ['website', 'bio']