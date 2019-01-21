from django import forms
from .models import Image,Comment,Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile','likes','pub_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','followers']
