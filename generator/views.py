from django.shortcuts import render
from django.http import HttpResponse
import random
import string                  
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepass = ''
    characters = list(string.ascii_lowercase)
    lenght = int(request.GET.get('lenght',8))
    if request.GET.get('uppercase') == 'on':
        characters = list(string.ascii_letters)  
    if request.GET.get('numbers') == 'on':
        characters.extend(list(string.digits))    
    if request.GET.get('special') == 'on': 
        characters.extend(list(string.punctuation)) 
    for i in range(lenght):
        thepass += random.choice(characters)   
    return render(request, 'generator/password.html', {'password':thepass})

def aboutus(request):
    return render(request, 'generator/aboutus.html')