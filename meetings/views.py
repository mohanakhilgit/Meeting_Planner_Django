from django.shortcuts import render, redirect, get_object_or_404
from .form import MeetingForm

# Create your views here.

from .models import Meeting, Room


def details(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)

    return render(request, 'meetings/details.html', {"meeting": meeting})


def rooms_list(request):
    return render(request, 'meetings/rooms_list.html', {'rooms': Room.objects.all()})


def create_form(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = MeetingForm()
    return render(request, 'meetings/form.html', {'form': form})
