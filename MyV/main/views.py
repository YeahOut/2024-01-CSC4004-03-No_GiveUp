from django.shortcuts import render
from django.http import HttpResponse

def main_1(request):
    return render(request, 'main/main_1.html')

def main_2(request):
    return render(request,'main/loading.html')

def main_3(request):
    return render(request, 'main/main_3.html')