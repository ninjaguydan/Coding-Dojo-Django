from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "name" : "Daniel",
        "fav_color" : "Purple",
        "pets" : ["cat", "dog", "fish"]
    }
    return render(request, "index.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"placeholder to display the blog number: {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request, num):
    return redirect('/')