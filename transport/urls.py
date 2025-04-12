from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('schedule/', views.schedule_transport, name='schedule_transport'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('confirmation/', views.confirmation, name='confirmation'),path('home/', views.home, name='home'),
    path('cancel_transport/', views.cancel_transport, name='cancel_transport'),
     path('cancel_transport/<int:transport_id>/', views.cancel_transport, name='cancel_transport'),
    path('rate/', views.rate_experience, name='rate_experience'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
]
