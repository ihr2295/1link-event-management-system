from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL points to index view
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),  # Corrected line
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('create_event/', views.create_event, name='create_event'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('bookings/', views.bookings, name='bookings'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('book_event/<int:event_id>/', views.book_event, name='book_event'),  # New URL pattern
    path('manage_events/', views.manage_events, name='manage_events'),
    path('manage_events/edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('manage_events/delete/<int:pk>/', views.delete_event, name='delete_event'),
    path('contact/', views.contact_view, name='contact'),
]
