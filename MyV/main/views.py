from django.shortcuts import render
from django.http import HttpResponse
from .awsInMain import upload_to_s3,downloadFile
from .maxminAnalyze import maxminAnalyze
from .sportify_api import sportify


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
    user = request.user
    #다시 추천 받을 때, 만약 최고음 최저음 분석을 한 번 했더라면 그냥 바로 디비 정보로 sportify만 돌리게하기 (리브로사 안쓰고!)
    # #userNoteInfo = UserMaxMinNote.objects.filter(user=user).order_by('-id').first()  # 가장 마지막 정보만 가져오기
    # if UserMaxMinNote == 'NoneType':
    #     maxminAnalyze(user)
    maxminAnalyze(user)
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