from django import forms
from .models import Custom_User

class Registration_Form(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'user_type', 'profile_picture', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'user_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Enter Profile Picture'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        }
    
    def username_clean_data(self):
        username = self.cleaned_data.get('username')
        if Custom_User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")
        return username
    
    def email_clean_data(self):
        email = self.cleaned_data.get('email')
        if Custom_User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists. Please choose a different one.")
        return email


class Login_Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
