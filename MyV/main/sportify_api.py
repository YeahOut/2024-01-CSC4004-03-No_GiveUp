from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

from matplotlib.image import imread
import matplotlib.pyplot as plt
import urllib.request

##model import 하기
from signup.models import UserPreferences
from main.models import UserMaxMinNote

def sportify(user):
    client_id = "0a3419c6f1934f9c85e6f0381335c2b0"
    client_secret = "2456e82f096b461da806ff45aeac645b"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    #윤하 박효신 아이유 뉴진스 데이식스
    seed_artist = ["spotify:artist:6GwM5CHqhWXzG3l5kzRSAS", "spotify:artist:57htMBtzpppc1yoXgjbslj",
                "spotify:artist:3HqSLMAZ3g3d5poNaI7GOU", "spotify:artist:6HvZYsbFfjnjFrWF950C9d",
                "spotify:artist:5TnQc2N1iKlFjYD7CPGvFc"]
    
    key_dict = {'C' : 0, 'C#' : 1, 'D' : 2, 'D#' : 3, 'E' : 4, 'F' : 5,
            'F#' : 6, 'G' : 7, 'G#' : 8, 'A' : 9, 'A#' : 10, 'B' : 11}

    userNoteInfo = UserMaxMinNote.objects.get(user=user) #db에서 정보 가져오기
    user_min_note = userNoteInfo.min_note
    user_max_note = userNoteInfo.max_note
    userPreferenceInfo = UserPreferences.objects.get(user=user)
    user_mood = userPreferenceInfo.mood
    user_energy = userPreferenceInfo.energy
    user_tmpo = userPreferenceInfo.tempo

    input_mood = user_mood
    input_energy = user_energy
    input_tmpo = user_tmpo
    min_key = key_dict[user_min_note[:len(user_min_note) - 1]]
    max_key = key_dict[user_max_note[:len(user_max_note) - 1]]

    min_mood = input_mood / 10 - 0.2
    max_mood = input_mood / 10 + 0.2
    min_energy = input_energy / 10 - 0.2
    max_energy = input_energy / 10  + 0.2
    min_tmpo = input_tmpo / 10 - 0.2
    max_tmpo = input_tmpo / 10 + 0.2
    min_key = min_key - 1
    max_key = max_key + 1
    min_popularity = 60
    recommendation_songs_cnt = 3


    recommended = sp.recommendations(limit=recommendation_songs_cnt, market='KR', seed_artists=seed_artist,
                                    min_danceability=min_mood, max_danceability=max_mood,
                                    min_energy=min_energy, max_energy=max_energy,
                                    min_tmpo=min_tmpo, max_tmpo=max_tmpo,
                                    min_key=min_key, max_key=max_key)
    tracks = recommended['tracks']

    #추천 결과
    song_names = [] #곡명
    song_urls = [] #spotify 곡페이지 url
    img_urls = [] #이미지 url
    img_dirs = [] #이미지jpg 저장 경로
    preview_urls = [] #미리듣기 url

    cnt = 1
    for track in tracks:
        song_url = track['external_urls']['spotify']
        song_name = track['name']
        preview_url = track['preview_url']
        img_url = track['album']['images'][0]['url']
        img_save_loc = "./img" + str(cnt) + ".jpg"
        urllib.request.urlretrieve(img_url, img_save_loc)
        image = imread(img_save_loc)

        song_names.append(song_name)
        song_urls.append(song_url)
        img_urls.append(img_url)
        img_dirs.append(img_url)
        preview_urls.append(preview_url)

        print(cnt,"######################")
        print(preview_url)
        print(song_url)
        print(img_url)
        print(song_name)

        cnt += 1

    print(song_names)
    print(song_urls)
    print(img_urls)
    print(preview_urls)

    if len(song_names) < 3:
        print("추천받은 곡 부족")

    for i in range(recommendation_songs_cnt - len(song_names)):
        img_urls.append("./tmp_img.png")
