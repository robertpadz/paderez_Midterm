from django.shortcuts import render
from django.http import HttpResponse

def jobroles(request):
    context = {
        'a' : 'reporting executive',
        'b' : 'business analyst',
        'c' : 'data analyst',
        'd' : 'statistician',
        'e' : 'data scientist',
        'f' : 'data engineer/data architect',
        'g' : 'machine learning engineer',
        'h' : 'big data engineer'
     }


    return render(request, "midterma.html", context)