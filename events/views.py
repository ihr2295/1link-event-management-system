from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, EventForm
from django.contrib.auth.decorators import login_required
from .models import Event
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Event, Booking

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
            messages.success(request, 'You have registered successfully. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('user_dashboard')  # or any page you want to redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('login')

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'users/events.html', {'events': events})

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'users/event_detail.html', {'event': event})

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
            messages.success(request, 'Event created successfully.')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'users/create_events.html', {'form': form})  # Check the path here

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'users/bookings.html', {'bookings': user_bookings})

@login_required
def user_dashboard(request):
    events = Event.objects.all()
    return render(request, 'users/index.html', {'events': events})

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    booking, created = Booking.objects.get_or_create(user=request.user, event=event)
    if created:
        messages.success(request, 'You have successfully booked the event.')
    else:
        messages.info(request, 'You have already booked this event.')
    return redirect('bookings')
