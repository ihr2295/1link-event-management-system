from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL points to index view
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('create_event/', views.create_event, name='create_event'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('bookings/', views.bookings, name='bookings'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
]
