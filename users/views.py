from django.contrib.auth import login, logout as auth_logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('login')

