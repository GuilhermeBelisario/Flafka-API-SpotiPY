import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import time

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

try:
    
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
    result = sp.search(q='Iron Maiden', type='artist')
    artist = result['artists']['items'][0]

    artist_id = artist['id']
    artist_genres = artist['genres']
    top_tracks = sp.artist_top_tracks(artist_id)
    tracks = []

    for idc, track in enumerate(top_tracks['tracks']):
        tracks.append(f"{idc + 1}. {track['name']} - {track['popularity']}")

    band_information = {'Name': 'Iron Maiden' , 'Gender': artist_genres , 'TopSong': tracks} 
    genero = band_information['Gender']
    nome = band_information['Name']

except:
    pass    

finally:

    time.sleep(5)

