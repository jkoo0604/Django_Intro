from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def index(request):
    return render(request,'index.html')

def display(request):
    print(request.POST)

    strawberry = request.POST['strawberry']
    raspberry = request.POST['raspberry']
    apple = request.POST['apple']
    studentname = request.POST['username']
    studentid = request.POST['studentid']
    
    itemcount = int(strawberry)+ int(raspberry)+ int(apple)

    context = {
        'strawberry': strawberry,
        'raspberry': raspberry,
        'apple': apple,
        'studentname': studentname,
        'studentid': studentid,
        'itemcount': itemcount,
        "datetime": strftime("%B %d %Y\n%H:%M %p", gmtime())
    }

    print(context)
    print(f"Charging {studentname} for {itemcount} fruits")
    return render(request,'show.html', context)