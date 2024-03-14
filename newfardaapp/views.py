from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from .forms import *


@login_required
def ProfileView(request):
    if request.method == 'POST':
        profile = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        skills = SkillsForm(request.POST, request.FILES, instance=request.user.profile)
        networks = NetworksForm(request.POST, request.FILES, instance=request.user.profile)
        if profile.is_valid():
            profile.save()
            skills.save()
            networks.save()

    else:
        profile = ProfileForm(instance=request.user.profile)
        skills = SkillsForm(instance=request.user.profile)
        networks = NetworksForm(instance=request.user.profile)

    return render(request, 'index.html', {'profile': profile, 'skills':skills, 'networks':networks})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"