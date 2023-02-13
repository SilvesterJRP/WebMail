from django.urls import path
from Mailer import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.helloviewer, name="helloviewer"),
    path("mail", views.reademail, name="reademail"),
    path("compose", views.composemail, name="composemail")
]