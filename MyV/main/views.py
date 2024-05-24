from django.shortcuts import render
from django.http import HttpResponse
from .awsInMain import upload_to_s3,downloadFile
from .maxminAnalyze import maxminAnalyze
def main_1(request):
    return render(request, 'main/main_1.html')

def upload_max_min(request):
    if request.method == 'POST':
        min_file = request.FILES.get('min_file', None)
        max_file = request.FILES.get('max_file', None)
        
        if min_file and max_file:
            user = request.user
            upload_to_s3(min_file, max_file, user)
            return HttpResponse("Files uploaded successfully")
        else:
            return HttpResponse("Failed to upload files")
    
    return HttpResponse("Failed to upload files")

def main_2(request):
    user = request.user
    maxminAnalyze(user)
    return render(request,'main/loading.html')

def main_3(request):
    return render(request, 'main/main_3.html')