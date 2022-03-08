from django.contrib import admin
from django.urls import path
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home, name="home"),
    path("signup", views.register, name = "signup"),
    path("login", views.login, name = "login"),
    path('index', views.index, name = "index"),
    path('list', views.Appointment_List, name = "list"),
    path('contact', views.Contact, name = "contact"),
    path('service', views.Services, name = "service"),
    path('logout', views.logout, name = "logout"),
    path('profile', views.Profile, name = "profile"),


]
