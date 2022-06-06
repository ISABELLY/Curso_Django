from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME 1')

def sobre(request):
    return HttpResponse('sobre')
    
def contato(request):
    return HttpResponse('contato')    

