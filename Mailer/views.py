from django.shortcuts import render
from django.utils.timezone import datetime
import re

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World From Django!!!")

def helloviewer(request, name):
    return render(
        request,
        'Mailer/hellothere.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def reademail(request):
    return render(
        request,
        'Mailer/openemail.html'
    )

def composemail(request):
    return render(
        request,
        'Mailer/ComposeMail.html'
    )