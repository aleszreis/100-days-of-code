from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scrapping Billboard
date = input("Which year do you want to travel to? Type the date as YYYY-MM-DD: ")

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
soup = BeautifulSoup(response.text, 'html.parser')

song_names = soup.find_all(name='span', class_='chart-element__information__song')
song_names = [title.getText() for title in song_names]

# Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri='http://example.com',
        client_id='CLIENT_ID_HERE',
        client_secret='CLIENT_SECRET_HERE',
        show_dialog=True,
        cache_path=".cache"))

user_id = sp.current_user()["id"]

# Adding Tracks
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist["id"], song_uris)