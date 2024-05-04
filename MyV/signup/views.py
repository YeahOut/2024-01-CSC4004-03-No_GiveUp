from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def signup1(request):
    return render(request, 'signup/signup1.html')

def signup2(request):
    return render(request, 'signup/signup2.html')

def signup3(request):
    return render(request, 'signup/signup3.html')