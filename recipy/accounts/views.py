from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm


from django.contrib.auth.views import LogoutView

from django.contrib import messages

def login_view(request):

    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("/")
        # redirect

    return render(request, "authenticate.html", {"form": form, "title": title})


def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        email = form.cleaned_data.get("email")
        terms = form.cleaned_data.get("terms")

        user.set_password(password)
        user.save()

        newuser = authenticate(username=username, password=password)

        login(request, newuser)


        return redirect("/")
        # redirect

    context = {"form":form,"title":title}
    return render(request, "authenticate.html", context)

def logout_view(LogoutView):

    # TRY TO RETURN MESSAGE TO THE TEMPLATE
    def get_next_page(self):
        next_page = super(logout_view, self).get_next_page()
        messages.add_message(
            self.request, messages.SUCCESS,
            'You successfully log out!'
        )
        return next_page

    # LOGOUT AND REDIRECT
    logout(LogoutView)
    return redirect("/")


