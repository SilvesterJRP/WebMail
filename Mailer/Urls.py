from django.urls import path
from Mailer import views

urlpatterns = [
    path("", views.home, name="home"),
]