from django.shortcuts import render,redirect
from django.http import HttpResponse
from .analyzing_file import process_file
from .aws import downloadFile, upload_to_s3, makingBucket,deleteBucket
from .models import UserVocalInfo, SelectedPlaylist
from main.models import PlaylistInfo

# Create your views here.

def analyzePage(request):
    user = request.user
    context = {'user':user}
    return render(request,'modal/analyze.html', context)

#AWS s3에 업로드하는 함수
def upload_analyze_file(request):
    if request.method == 'POST':
        mySound_file = request.FILES.get('mysound_file', None)
        compareSound_file = request.FILES.get('comparesound_file', None)
        
        if mySound_file and compareSound_file:
            upload_to_s3(mySound_file, compareSound_file)
            return HttpResponse("Files uploaded successfully")
        else:
            return HttpResponse("Failed to upload files")
    
    return HttpResponse("Failed to upload files")


def vocalResult(request):
    #context = maxminAnalysis(request)
    downloaded = downloadFile() #음원 다운로드 받기
    print("##전달 성공##")

    if (downloaded==1):
        max_note, min_note, start_t, best_st, best_ed, score = process_file()
        user = request.user  # 현재 로그인한 사용자에 접근하기 위한 용도..
        context = {'max':max_note, 'min':min_note, 'start_t': start_t, 'best_st': int(best_st), 'best_ed':int(best_ed), 'score':score, 'user': user}
        saveInfo = UserVocalInfo(user= user, max_note=max_note, min_note=min_note)
        saveInfo.save()
    else :
        print("##파일이 다운로드 되지 않았음##")
    return render(request, 'modal/analyze_result.html', context)

#####playlist View 
def playlistPage(request):
    if request.method == "POST":
        album_id = request.POST.get('selected_album_id')
        
        user = request.user
        playlist_info = PlaylistInfo.objects.filter(user=user).order_by('-id').first()
    
        if album_id == "1" :
            SelectedPlaylist.objects.create(user=user, img=playlist_info.img1, artist=playlist_info.artist1, title=playlist_info.title1)
        elif album_id == "2":
            SelectedPlaylist.objects.create(user=user, img=playlist_info.img2, artist=playlist_info.artist2, title=playlist_info.title2)
        elif album_id == "3":
            SelectedPlaylist.objects.create(user=user, img=playlist_info.img3, artist=playlist_info.artist3, title=playlist_info.title3)
        
        ##return은 예인이가 템플릿으로 바꾸면 될 것 같아용!
        return HttpResponse(f'{album_id}')