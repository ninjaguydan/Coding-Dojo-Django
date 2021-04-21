from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def handler(request):
     request.session['name'] = request.POST['name']
     request.session['location'] = request.POST['dojo_location']
     request.session['language'] = request.POST['fav_lang']
     request.session['message'] = request.POST['message']
     return redirect('/result/')


def result(request):
    # if request.method == "POST":
    #     name = request.POST["name"]
    #     location = request.POST["dojo_location"]
    #     language = request.POST["fav_lang"]
    #     message = request.POST["message"]
    # context = {
    #     "name" : name,
    #     "location" : location,
    #     "language" : language,
    #     "message" : message
    # }
    return render(request, "result.html")