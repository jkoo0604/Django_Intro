from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


# Create your views here.
def index(request):
    return redirect("/time_display")

def displaytime(request):
    context = {
        # "date": strftime("%b %d, %Y", gmtime()),
        # "time": strftime("%H:%M %p", gmtime())
        "datetime": strftime("%b %d, %Y\n%H:%M %p", gmtime()),
    }
    return render(request, 'timedisplay.html', context)