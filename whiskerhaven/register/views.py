from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            # Redirect to login only if the form is valid
            return redirect('/login')
    else:
        form = RegisterForm()

    # If the form is not valid or if it's a GET request, render the form with errors if any
    return render(response, "register/register.html", {'form': form})
