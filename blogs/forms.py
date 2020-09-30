from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms

from .models import Comment, Blog


class CommentForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='This email will be used in case author wants to contact you.')
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        banned = ['self', 'api', 'login', 'logout', 'register', 'dashboard', 'about', 'contact', 'dev-admin', 'ckeditor']
        if username in banned:
            raise forms.ValidationError('You cannot use this username.')
        return username


class UpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CretePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'meta', 'thumb', 'content', 'published']