from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['count'] = 0
    return render(request, "index.html")

def generate(request):
    request.session['count'] += 1
    #Generate random word
    request.session['unique_id'] = get_random_string(length=14)
    return render(request, "index.html")