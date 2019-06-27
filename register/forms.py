from django import forms
from django.contrib.auth import authenticate,get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.Textarea(attrs={'class':'input100','placeholder':"username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100','placeholder':"password"}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.Textarea(attrs={'class':'input100','placeholder':"username"}))
    email = forms.EmailField(widget=forms.Textarea(attrs={'class':'input100','placeholder':"email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100','placeholder':"password"}))
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'input100','placeholder':"password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already exists")
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print(password,password2)
        if password2 != password:
            raise forms.ValidationError("Password must match")
        return data
