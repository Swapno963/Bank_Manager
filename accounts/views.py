from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login


# Create your views here.
class UserRegistrationView(FormView):
    template_name = ''
    form_class = UserRegistrationForm
    success_url = ''


    def form_valid(self, form):
        user = form.save() # UserRegistrationForm save korber por user k return korbe
        login(user) # form valid hole user k login korano hobe
        return super().form_valid() # nija nija k call korbe jodi sob tik thake




    