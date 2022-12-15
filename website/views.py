from django.shortcuts import render
from meetings.models import Meeting  # type:ignore

# Create your views here.

from django.http import HttpResponse


def welcome(request):
    return render(request, 'website/home.html', {"meetings": Meeting.objects.all()})
