import logging
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


logger = logging.getLogger(__name__)


def register(request):
    context = {
        "registration_form": UserCreationForm(),
    }
    return render(request, 'questions/register.html', context)
