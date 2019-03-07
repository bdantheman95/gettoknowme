from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'get_to_know_brandon/home.html', context)


def imfrom(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'get_to_know_brandon/imfrom.html', context)


def ilike(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'get_to_know_brandon/ilike.html', context)


