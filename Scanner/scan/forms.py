from django import forms

# forms.py
# from django import forms
from .models import Image,User


class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    id = forms.UUIDField(label='User ID')


class ImageForm(forms.ModelForm):

    class Meta:
        model =Image
        fields = [ 
            'image','img_name',]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','blood_group','ph_no','email','age','address']
        

# class ImageDeleteForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = [] 