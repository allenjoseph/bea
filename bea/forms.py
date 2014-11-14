from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(
                widget=forms.TextInput(attrs={'class' : 'form-control'}),
                error_messages={'required': 'Ingresa tu usuario'}
            )
    password = forms.CharField(
                widget=forms.PasswordInput(attrs={'class' : 'form-control'}),
                error_messages={'required': 'Ingresa tu password'}
            )
        