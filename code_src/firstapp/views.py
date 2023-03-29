from django.shortcuts import render



# Create your views here.

def index(request):
    return render(request, 'firstapp/index.html')

def connexion(request):
    return render(request, 'firstapp/connexion.html')

def inscription(request):
    return render(request, 'firstapp/inscription.html')