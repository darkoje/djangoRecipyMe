from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm
from accounts.forms import (EditProfileForm, ProfileForm)
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


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

#PROFILE VIEW
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
        #profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)  # request.FILES is to show the selected image or file
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            # return redirect('accounts:view_profile')
            return redirect('/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'accounts/edit_profile.html', args)




# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('accounts:view_profile'))
#     else:
#         form = EditProfileForm(instance=request.user)
#         context = {'form': form}
#         return render(request, 'accounts/edit_profile.html', context)
