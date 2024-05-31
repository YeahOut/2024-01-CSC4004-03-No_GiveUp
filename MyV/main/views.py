from django.shortcuts import render
from django.http import HttpResponse
from .awsInMain import upload_to_s3,downloadFile
from .maxminAnalyze import maxminAnalyze
from .sportify_api import sportify

##async
from asgiref.sync import sync_to_async
import asyncio
##

def css(request):
    return render(request,'main/main_3.html')
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

async def main_2(request):
    user = request.user
    task1 = asyncio.ensure_future(maxminAnalyze(user))
    await asyncio.wait([task1])
    return render(request,'main/loading.html')

def main_3(request):
    user = request.user
    #song_names~preview_urls는 각각 리스트
    #userInfo는 max,min, mood, tmpo, energy 순으로 담긴 리스트
    song_names, song_urls, img_urls, preview_urls, artist, userInfo = sportify(user) 
    context = {
        'user' : user,
        'cover1' : img_urls[0],
        'cover2' : img_urls[1],
        'cover3' : img_urls[2],
        'title1' : song_names[0],
        'title2' : song_names[1],
        'title3' : song_names[2],
        'min' : userInfo[1],
        'max' : userInfo[0],
        'mood' : userInfo[2],
        'tmpo' : userInfo[3],
        'energy' : userInfo[4],
        'artist1' : artist[0],
        'artist2' : artist[1],
        'artist3' : artist[2],
        'preview1' : preview_urls[0],
        'preview2' : preview_urls[1],
        'preview3' : preview_urls[2],
    }   
    return render(request, 'main/main_3.html',context)

#########test########
def test(request):
    user = request.user
    sportify(user)
    return render(request, 'main/test.html')