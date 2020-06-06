from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def display(request):
    print(request.POST)

    username = request.POST['username']
    location = request.POST['locationdropdown']
    currentos = request.POST['oschoice']
    favlang = request.POST.getlist('favlanguage')
    opttext = request.POST['optionalcomment']
    
    context = {
        'username': username,
        'location': location,
        'currentos': currentos,
        'favlang': favlang,
        'opttext': opttext
    }

    print(context)
    return render(request,'show.html', context)