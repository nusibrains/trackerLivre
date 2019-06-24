from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# name=None => parametre optionnel utile pour générer des PDF
def home(request, name=None):
    if name:
        return HttpResponse('hello wolrd! %s' % name)
    else:
        return HttpResponse('coucou')
