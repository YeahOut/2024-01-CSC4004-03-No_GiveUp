from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
from matplotlib.image import imread
import matplotlib.pyplot as plt
import urllib.request

##model import 하기
from signup.models import UserPreferences
from main.models import UserMaxMinNote, PlaylistInfo


def sportify(user):
    client_id = "0a3419c6f1934f9c85e6f0381335c2b0"
    client_secret = "2456e82f096b461da806ff45aeac645b"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # 윤하 박효신 아이유 뉴진스 데이식스
    seed_artist = ["spotify:artist:6GwM5CHqhWXzG3l5kzRSAS", "spotify:artist:57htMBtzpppc1yoXgjbslj",
                   "spotify:artist:3HqSLMAZ3g3d5poNaI7GOU", "spotify:artist:6HvZYsbFfjnjFrWF950C9d",
                   "spotify:artist:5TnQc2N1iKlFjYD7CPGvFc"]

    key_dict = {'C': 0, 'C♯': 1, 'D': 2, 'D♯': 3, 'E': 4, 'F': 5,
                'F♯': 6, 'G': 7, 'G♯': 8, 'A': 9, 'A♯': 10, 'B': 11}

    # db에서 정보 가져오기 (최고음 최저음)
    userNoteInfo = UserMaxMinNote.objects.filter(user=user).order_by('-id').first()  # 가장 마지막 정보만 가져오기
    print("user:", user)
    user_min_note = userNoteInfo.min_note
    user_max_note = userNoteInfo.max_note

    # db에서 정보 가져오기 (회원 성향 정보)
    userPreferenceInfo = UserPreferences.objects.filter(user=user).order_by('-id').first()  # 가장 마지막 정보만 가져오기
    user_mood = userPreferenceInfo.mood
    user_energy = userPreferenceInfo.energy
    user_tmpo = userPreferenceInfo.tempo

    input_mood = user_mood
    input_energy = user_energy
    input_tmpo = user_tmpo
    min_key = key_dict[user_min_note[:len(user_min_note) - 1]]
    print(min_key)
    max_key = key_dict[user_max_note[:len(user_max_note) - 1]]
    female_key = 502 #0530
    male_key = 405 #0530
    #키 값 = 옥타브 * 100 + key_dict, 0530
    cmp_key = (min_key + 100 * int(user_min_note[-1]) + max_key + 100 * int(user_max_note[-1])) / 2 #0530

    min_mood = input_mood / 10 - 0.2
    max_mood = input_mood / 10 + 0.2
    min_energy = input_energy / 10 - 0.2
    max_energy = input_energy / 10 + 0.2
    min_tmpo = input_tmpo / 10 - 0.2
    max_tmpo = input_tmpo / 10 + 0.2
    min_key = min_key - 1
    max_key = max_key + 1
    min_popularity = 60 
    recommendation_songs_cnt = 3

    mood_string = ""
    energy_string = ""
    tempo_string = ""
    user_key_string = "" #0530

    if input_mood < 2:
        mood_string = "매우 차분한"
    elif input_mood < 4:
        mood_string = "차분힌"
    elif input_mood < 6:
        mood_string = "보통"
    elif input_mood < 8:
        mood_string = "활기찬"
    else:
        mood_string = "매우 활기찬"

    if input_energy < 2:
        energy_string = "매우 잔잔한"
    elif input_energy < 4:
        energy_string = "잔잔한"
    elif input_energy < 6:
        energy_string = "보통"
    elif input_energy < 8:
        energy_string = "강렬한"
    else:
        energy_string = "매우 강렬한"

    if input_tmpo < 2:
        tempo_string = "매우 느림"
    elif input_tmpo < 4:
        tempo_string = "느림"
    elif input_tmpo < 6:
        tempo_string = "보통"
    elif input_tmpo < 8:
        tempo_string = "빠름"
    else:
        tempo_string = "매우 빠름"

    if cmp_key > female_key :
        user_key_string = "여성 평균보다 높아요"
    elif cmp_key > male_key :
        user_key_string =  "여성 평균보다 낮고 남성 평균보다 높아요"
    else :
        user_key_string = "남성 평균보다 낮아요"
        
    recommended = sp.recommendations(limit=recommendation_songs_cnt, market='KR', seed_artists=seed_artist,
                                     min_danceability=min_mood, max_danceability=max_mood,
                                     min_energy=min_energy, max_energy=max_energy,
                                     min_tmpo=min_tmpo, max_tmpo=max_tmpo,
                                     min_key=min_key, max_key=max_key)
    tracks = recommended['tracks']

    # 추천 결과
    song_names = []  # 곡명
    song_urls = []  # spotify 곡페이지 url
    img_urls = []  # 이미지 url
    img_dirs = []  # 이미지jpg 저장 경로
    preview_urls = []  # 미리듣기 url
    artists = []

    cnt = 1
    for track in tracks:
        song_url = track['external_urls']['spotify']
        song_name = track['name']
        preview_url = track['preview_url']
        img_url = track['album']['images'][0]['url']
        artist = track['artists'][0]['name']
        # img_save_loc = "./img" + str(cnt) + ".jpg"
        # urllib.request.urlretrieve(img_url, img_save_loc)
        # image = imread(img_save_loc)

        song_names.append(song_name)
        song_urls.append(song_url)
        img_urls.append(img_url)
        img_dirs.append(img_url)
        preview_urls.append(preview_url)
        artists.append(artist)

        print(cnt, "######################")
        print(preview_url)
        print(song_url)
        print(img_url)
        print(song_name)
        print(artist)
        cnt += 1

    print(song_names)
    print(song_urls)
    print(img_urls)
    print(preview_urls)
    print(artists)
    print("#######" + artists[0])

    ####db전달
    playlist_info = PlaylistInfo(user=user)

    for i in range(len(song_names)):
        setattr(playlist_info, f'img{i + 1}', img_urls[i])
        setattr(playlist_info, f'artist{i + 1}', artists[i])
        setattr(playlist_info, f'title{i + 1}', song_names[i])
        setattr(playlist_info, f'songurl{i + 1}', song_urls[i])

    playlist_info.save()

    if len(song_names) < 3:
        for i in range(3 - len(song_names)):
            img_urls.append(".\static\main\images\tmp_img.png")
            song_name.appned(" ")
            song_url.append(" ")
            artist.appned(" ")
            preview_url.append(" ")

    for i in range(recommendation_songs_cnt - len(song_names)):
        img_urls.append(os.join.path(os.getcwd(), 'main', 'static', 'main', 'tmp_img.png'))

    return song_names, song_urls, img_urls, preview_urls, artists, [user_max_note, user_min_note, mood_string,
                                                                    tempo_string, energy_string]