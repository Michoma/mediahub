from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


# registration form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ensure password fields and username have bootstrap classes and placeholders
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})


# login form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'password')
    
    

# profile form : update on account profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'bio', 'profile_image')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

