from django import forms
from django.contrib.auth import (authenticate, get_user_model, login, logout)

from crispy_forms.helper import FormHelper


User = get_user_model()


class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'username'}), label="")
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'password'}), label="")

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # user_qs = User.objecs.filter(username=username) # user querry set
        # if user_qs.count() ==1:
        #     user = user_qs.first()

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(UserLoginForm, self).clean(*args,**kwargs)

    class Meta:
        # model = Recipy
        fields = ['username','password']


class UserRegisterForm(forms.ModelForm):

    #email = forms.EmailField(attrs={'placeholder': 'email'})
    email = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'placeholder': 'email'}), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), label="")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}), label="")

    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'username'}), label="")


    class Meta:
        model = User

        fields = [
            'email',
            'password',
            'confirm_password',
            'username'
            ]

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     email2 = self.cleaned_data.get("email2")

    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")
    #     return super(UserRegisterForm,self).clean(*args, **kwargs)

    # def clean_email2(self):
    #     email = self.cleaned_data.get("email")
    #     email2 = self.cleaned_data.get("email2")

    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")
    #     return email

