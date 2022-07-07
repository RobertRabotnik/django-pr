from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from users.models import CustomUser
from django import forms

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Повтор пароля'}))
    image = forms.ImageField(label='Аватар(не обязательно)',required=False,widget=forms.FileInput(attrs={'class':'form-control'}))


    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2','image')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))

    class Meta:
        model = CustomUser
        fields = ('username','email','password')



