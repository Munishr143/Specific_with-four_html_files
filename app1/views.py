from django.shortcuts import render

# Create your views here.
def First(request):
    return render(request, 'first.html')

def Second(request):
    return render(request, 'second.html')
