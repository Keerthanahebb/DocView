from django import forms

# forms.py
# from django import forms
from .models import Image,User


class ImageForm(forms.ModelForm):

    class Meta:
        model =Image
        fields = [ 'image','name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']