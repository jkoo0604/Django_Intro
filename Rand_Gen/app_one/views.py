from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return redirect('/random_word')

def generateword(request):

    if 'counter' in request.session:
        request.session['counter'] += 1
        # if request.session['counter'] == 0:
        #     rand_str=''
        # else:
        rand_str = get_random_string(length=14)
    else:
        request.session['counter'] = 0
        rand_str = ''
        # rand_str = get_random_string(length=14)
        
    context = {
        'counter': request.session['counter'],
        'rand_str': rand_str,
    }
    return render(request,'randomnum.html',context)

def resetcounter(request):
    del request.session['counter']
    # request.session['counter'] = -1
    # rand_str = ''
    # context = {
    #     'counter': request.session['counter'],
    #     'rand_str': rand_str,
    # }
    # return render(request,'randomnum.html',context)
    return redirect('/')