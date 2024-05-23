from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

from matplotlib.image import imread
import matplotlib.pyplot as plt
import urllib.request

client_id = "0a3419c6f1934f9c85e6f0381335c2b0"
client_secret = "2456e82f096b461da806ff45aeac645b"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

seed_artist = ["spotify:artist:6GwM5CHqhWXzG3l5kzRSAS", "spotify:artist:57htMBtzpppc1yoXgjbslj",
               "spotify:artist:4k5fFEYgkWYrYvtOK3zVBl", "spotify:artist:6HvZYsbFfjnjFrWF950C9d",
               "spotify:artist:4eh2JeBpQaScfHKKXZh5vO"]

input_mood = 0.1
input_energy = 0.5
input_tmpo = 0.5
input_key = 5

min_mood = input_mood - 0.2
max_mood = input_mood + 0.2
min_energy = input_energy - 0.2
max_energy = input_energy + 0.2
min_tmpo = 0
max_tmpo = 1
min_key = input_key - 1
max_key = input_key + 1
min_popularity = 60
recommendation_songs_cnt = 3


recommended = sp.recommendations(limit=recommendation_songs_cnt, market='KR', seed_artists=seed_artist,
                                 min_danceability=min_mood, max_danceability=max_mood,
                                 min_energy=min_energy, max_energy=max_energy,
                                 min_tmpo=min_tmpo, max_tmpo=max_tmpo,
                                 min_key=min_key, max_key=max_key)
tracks = recommended['tracks']

#추천 결과
songs = [] #곡명
img_urls = [] #이미지 url
img_dirs = [] #이미지jpg 저장 경로


cnt = 1
for track in tracks:
    song_url = track['external_urls']
    song_name = track['name']
    preview_url = track['preview_url']
    img_url = track['album']['images'][0]['url']
    img_save_loc = "./img" + str(cnt) + ".jpg"
    urllib.request.urlretrieve(img_url, img_save_loc)
    image = imread(img_save_loc)

    songs.append(song_name)
    img_urls.append(img_url)
    img_dirs.append(img_url)

    print(cnt,"######################")
    print(preview_url)
    print(song_url)
    print(img_url)
    print(song_name)

    cnt += 1

for i in range(recommendation_songs_cnt - len(songs)):
    img_dirs.append("./tmp_img.png")
