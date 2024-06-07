from django.shortcuts import render, redirect
from .forms import SignUpForm, EventForm
from .models import Event
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def login_view(request):
    # Implement login logic
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def change_password(request):
    return render(request, 'users/change_password.html')

@login_required
def bookings(request):
    return render(request, 'users/bookings.html')

@login_required
def user_dashboard(request):
    return render(request, 'users/index.html')
