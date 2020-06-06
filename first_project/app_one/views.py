from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # return render(request,"index.html")
    return HttpResponse("placeholder to later display a list of all blogs")

def hello_name(request, name):
    context = {
        "htmlname": name,
        "namelist": ["Alice", "Bob", "Charlie", "David"]
    }
    return render(request, "helloname.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, my_int):
    return HttpResponse(f"placeholder to display blog number: {my_int}")

def edit(request, my_int):
    return HttpResponse(f"placeholder to edit blog {my_int}")

def destroy(request, my_int):
    return redirect("/")