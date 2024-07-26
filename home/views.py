from django.shortcuts import render 


# Create your views here.

def home(request):
    # print('home')
    context = {
           'text': 'WE ARE AT HOME',
           'tittle': 'HOME'

    }
    return render(
        request,
        'home/index.html',
        context,
        
    )