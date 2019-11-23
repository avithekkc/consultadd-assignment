from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            messages.success(request, f'Your account has ben created! Login to access the blog!')
            return redirect('login')
    else:
            form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})
