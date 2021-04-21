from django.shortcuts import render
import datetime

# Create your views here.
def time_display(request):
    time = datetime.datetime.now()
    context = {
        "date" : time.strftime("%a, %b %d, %Y"),
        "time" : time.strftime("%I:%M:%S %p")
        # "date" : "%s/%s/%s" % (time.month, time.day, time.year),
        # "time" : "%s:%s:%s" % (time.hour, time.minute, time.second)
    }
    return render(request, "index.html", context)
