from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .analyzing_file import process_file
from .aws import downloadFile, upload_to_s3, makingBucket, deleteBucket
from .models import UserVocalInfo, SelectedPlaylist
from main.models import PlaylistInfo

def analyzePage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'modal/analyze.html', context)

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
    downloaded = downloadFile()
    print("##전달 성공##")

    if downloaded == 1:
        max_note, min_note, start_t, best_st, best_ed, score = process_file()
        user = request.user
        context = {'max': max_note, 'min': min_note, 'start_t': start_t, 'best_st': int(best_st), 'best_ed': int(best_ed), 'score': score, 'user': user}
        saveInfo = UserVocalInfo(user=user, max_note=max_note, min_note=min_note)
        saveInfo.save()
    else:
        print("##파일이 다운로드 되지 않았음##")
    return render(request, 'modal/analyze_result.html', context)

def playlistPage(request):
    user = request.user
    if request.method == "POST":
        album_id = request.POST.get('selected_album_id')
        playlist_info = PlaylistInfo.objects.filter(user=user).order_by('-id').first()
    
        if album_id == "1" :
            SelectedPlaylist.objects.create(user=user, img=playlist_info.img1, artist=playlist_info.artist1, title=playlist_info.title1, song_url=playlist_info.songurl1)
        elif album_id == "2":
            SelectedPlaylist.objects.create(user=user, img=playlist_info.img2, artist=playlist_info.artist2, title=playlist_info.title2, song_url=playlist_info.songurl2)
        elif album_id == "3":
            SelectedPlaylist.objects.create(user=user, img=playlist_info.img3, artist=playlist_info.artist3, title=playlist_info.title3, song_url=playlist_info.songurl3)
        
        return redirect('playlistPage')  # POST 요청 후 리디렉션

    playlists = SelectedPlaylist.objects.filter(user=user).order_by('-id')
    paginator = Paginator(playlists, 4)  # 한 페이지에 5개의 플레이리스트를 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user': user
    }
    return render(request, 'modal/playlist.html', context)
