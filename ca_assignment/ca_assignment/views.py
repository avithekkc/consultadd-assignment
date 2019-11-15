from django.http import HttpResponse
from django.shortcuts import render
from  . import signup_form


def signup(request):
    form = signup_form.signupForm
    if request.method == "POST":
        form = signup_form.signupForm(request.POST)
        if form.is_valid():
            print('NAME = ', form.cleaned_data['name'])
            print('EMAIL = ', form.cleaned_data['email'])
            print('PASSWORD = ', form.cleaned_data['password'])
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'index.html')
