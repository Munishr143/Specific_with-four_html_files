from django.shortcuts import render

# Create your views here.
def Third(request):
    return render(request, 'third.html')

def Fourth(request):
    return render(request, 'fourth.html')