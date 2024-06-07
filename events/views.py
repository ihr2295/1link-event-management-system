from django.shortcuts import render, redirect
from .forms import SignUpForm, EventForm
from .models import Event
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('user_dashboard')  # or any page you want to redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'conditions.html')
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
