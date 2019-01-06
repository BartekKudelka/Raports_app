from django.contrib.auth import login as auth_login, authenticate
from raports_app.polls.forms import SignUpForm, EditProfileForm, CustomChangePasswordForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logged_out(request):
    return render(request, 'logged_out.html')


@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = CustomChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomChangePasswordForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })


@login_required(login_url='/login/')
def show_profile(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required(login_url='/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(request.POST, instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

