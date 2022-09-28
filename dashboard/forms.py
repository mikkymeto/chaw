from django import forms
from django.forms import ModelForm 
from .models import Profile


STATE = [
    ('Abia', 'abia'),
    ('Adamawa', 'adamawa'),
    ('Bayelsa', 'bayelsa'),
    ('Lagos', 'lagos'),
    ('Kaduna', 'kaduna'),
]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','phone','address','city','state','profile_pix']
        Widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'Placeholder': 'First Name is required'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'Placeholder': 'Last Name is required'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'Placeholder': 'Email is required'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'Placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'Placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'Placeholder': 'City'}),
            'state': forms.Select(attrs={'class':'form-control', 'Placeholder': 'State'}, choices=STATE),
            'profile_pix': forms.FileInput(attrs={'class':'form-control'}),
        
        }
