from django.shortcuts import render

# Create your views here.

# events/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# events/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking
from django.contrib.auth.decorators import login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Booking.objects.create(user=request.user, event=event)
    return redirect('event_detail', event_id=event.id)
