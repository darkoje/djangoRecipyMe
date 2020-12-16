from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)

from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm
from accounts.forms import (EditProfileForm, ProfileForm)

#we need this to fetch options
from accounts.models import UserProfile


# def prepare_for_preselect(saved_options):
#     data_for_preselect = []
#     for option in saved_options:
#         option = option.lower().replace(" ","-")
#         data_for_preselect.append(option)

#     if len(data_for_preselect) == 1:
#         data_for_preselect = "'" + data_for_preselect[0] + "'"
#     return data_for_preselect


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
        #confirm_password = form.cleaned_data.get("confirm_password")
        #email = form.cleaned_data.get("email")
        #terms = form.cleaned_data.get("terms")
        user.set_password(password)
        user.save()

        newuser = authenticate(username=username, password=password)
        login(request, newuser)

        # redirect to profile
        return redirect("/profile/edit")


    context = {"form":form,"title":title}
    return render(request, "authenticate.html", context)


@login_required
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


#PROFILE VIEW
@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


#EDIT PROFILE
@login_required
def edit_profile(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            try:
                custom_form.save()
                return redirect('/profile/')

            except:
                pass

    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {}
        args['form'] = form
        args['profile_form'] = profile_form
        args['user'] = request.user

        # RENDER THE EDIT PROFILE FORM
        return render(request, 'accounts/edit_profile.html', args)
