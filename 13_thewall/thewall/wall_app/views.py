from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def wall(request):
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['userid'])
    messages = Message.objects.all()
    comments = Comment.objects.all()
    context = {
        'user': user,
        'messages' : messages,
        'comments' : comments,
        }
    return render(request, "wall.html", context)

def post_message(request):
    user  = User.objects.get(id = request.session['userid'])
    Message.objects.create(content = request.POST['message'], user = user)
    return redirect("/wall/")

def destroy_message(request):
    message_to_destroy = Message.objects.get(id = request.POST['msg_id'])
    message_to_destroy.delete()
    return redirect("/wall/")

def post_comment(request):
    message = Message.objects.get(id = request.POST['msg_id'])
    user  = User.objects.get(id = request.session['userid'])
    Comment.objects.create(content = request.POST['message'], user = user, message = message)
    context = {
        "messages" : Message.objects.all()
    }
    return render(request, "wall-partial.html", context)
