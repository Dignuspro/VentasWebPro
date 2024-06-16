from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/login/'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
