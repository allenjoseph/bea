from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(
                widget=forms.TextInput(attrs={'class' : ''}),
                error_messages={'required': 'Ingresa tu usuario'}
            )
    password = forms.CharField(
                widget=forms.PasswordInput(attrs={'class' : ''}),
                error_messages={'required': 'Ingresa tu password'}
            )
        