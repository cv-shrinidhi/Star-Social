from django.shortcuts import render
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # after successful registration, when the user has hit the sign up button, it should take to the login page
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
