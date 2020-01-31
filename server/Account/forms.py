from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Account
# from Image.models import Image


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'field',
        'type': 'text',
        'placeholder': 'Login',
    }))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'field',
            'type': 'password',
            'placeholder': 'Password',
        })
    )


# class AccountInfoForm(forms.ModelForm):
#     avatar = forms.FileField(allow_empty_file=True)
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()

class AccountInfoForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'avatar']
    avatar = forms.FileField(allow_empty_file=True)

    def clean_avatar(self):
        value = self.cleaned_data['avatar']
        print(value)
        return value

#         widgets = {
#             'first_name': forms.widgets.Input(
#                 attrs={
#                     'class': 'yo_info',
#                     'type': 'text',
#                     'placeholder': 'Name',
#                 }
#             ),
#             'last_name': forms.widgets.Input(
#                 attrs={
#                     'class': 'yo_info',
#                     'type': 'text',
#                     'placeholder': 'Surname'
#                 }
#             ),
#             'email': forms.widgets.EmailInput(
#                 attrs={
#                     'class': 'yo_info',
#                     'type': 'email',
#                     'placeholder': 'E-mail'
#                 }
#             ),
#         }


class AccountRegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(
            strip=False,
            widget=forms.PasswordInput(
                attrs={
                'class': 'field',
                'type': 'password',
                'placeholder': 'Password confirm',
                }
            )
    )
    class Meta:
        model = Account
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'username': forms.widgets.Input(
                attrs={
                    'class': 'field',
                    'type': 'text',
                    'placeholder': 'Login'
                }
            ),
            'password': forms.widgets.PasswordInput(
                attrs={
                    'class': 'field',
                    'type': 'password',
                    'placeholder': 'Password'
                }
            ),
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password doesn't confirm.")

        return password_confirm

    def save(self, commit=True):
        obj = super().save(commit=False)
        password = self.cleaned_data.get('password')

        obj.set_password(password)
        obj.is_active = False

        if commit:
            obj.save()

        return obj
