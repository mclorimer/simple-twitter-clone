from django import forms
from django.core.exceptions import ValidationError


from users.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
    
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput())
    
    
    
    
    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('Passwords must match')
        
        else:
            self.cleaned_data['password'] = self.cleaned_data['password1']
            self.cleaned_data.pop('password1')
            self.cleaned_data.pop('password2')
            
        return self.cleaned_data


class UserLoginForm(forms.Form):
    
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())



