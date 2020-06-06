from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
    if not 'totalscore' in request.session:
        request.session['totalscore'] = 0
    if not 'activitystr' in request.session:
        request.session['activitystr'] = []
    if not 'totalmoves' in request.session:
        request.session['totalmoves'] = 0
    if not 'result' in request.session:
        request.session['result'] = ''

    context = {
        'totalscore': request.session['totalscore'],
        'activitystr': request.session['activitystr'],
        'totalmoves': request.session['totalmoves'],
        'result': request.session['result']
    }
    return render(request,'index.html',context)


def process_money(request, location):
    placelist = {
        'Farm': [10, 20],
        'Cave': [5, 10],
        'House': [2, 5],
        'Casino': [-50, 50]
    }
    temp_str = ''
    if location in placelist:
        score = random.randint(placelist[location][0], placelist[location][1])
        print(score) 

        if score > 0:
            temp_str = f"Earned {score} golds from the {location}! ({strftime('%Y/%m/%d %H:%M %p', gmtime())})"
        elif score == 0:
            temp_str = f"Entered a casino and earned 0 gold. ({strftime('%Y/%m/%d %H:%M %p', gmtime())})"
        else:
            temp_str = f"Entered a casino and lost {score * -1} golds. ({strftime('%Y/%m/%d %H:%M %p', gmtime())})"
        
        request.session['totalscore']+=score
        request.session['activitystr'] = [temp_str] + request.session['activitystr']
        request.session['totalmoves']+=1

        result = ''
        if 'targetmoves' in request.session and 'targetscore' in request.session:
            if request.session['totalmoves'] >= request.session['targetmoves']:
                if request.session['totalscore'] < request.session['targetscore']:
                    result = f"You failed to earn {request.session['targetscore']} golds in {request.session['targetmoves']} moves. Try again."
                    request.session['totalmoves']=0
                    request.session['totalscore']=0
            elif request.session['totalscore'] >= request.session['targetscore']:
                result = f"You have earned more than {request.session['targetscore']} golds in less than {request.session['targetmoves']} moves. You win."
                request.session['totalmoves']=0
                request.session['totalscore']=0
        request.session['result'] = result
        return redirect('/')
    else:
        return redirect('/')

def reset_score(request):
    # if  'totalscore' in request.session:
    #     del request.session['totalscore']
    # if  'activitystr' in request.session:
    #     del request.session['activitystr']
    # if  'totalmoves' in request.session:
    #     del request.session['totalmoves']
    # if  'targetmoves' in request.session:   
    #     del request.session['targetmoves']
    # if 'targetscore' in request.session:
    #     del request.session['targetscore']
    request.session.flush()
    return redirect('/')

def set_target(request):
    try:
        request.session['targetmoves'] = int(request.POST['targetmoves'])
        request.session['targetscore'] = int(request.POST['targetscore'])
        request.session['totalscore'] = 0
        request.session['activitystr'] = []
        request.session['totalmoves'] = 0
    except:
        print('Invalid targets')
    
    return redirect('/')
        