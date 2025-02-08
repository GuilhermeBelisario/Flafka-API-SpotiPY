from spotipy.oauth2 import SpotifyClientCredentials
import pytest
import spotipy
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do .env
load_dotenv()

@pytest.fixture
def spotify_credentials():
    """Fixture que retorna as credenciais da API Spotify."""
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    return client_id, client_secret

def test_client_id_and_client_secret_is_not_none(spotify_credentials):

    client_id, client_secret = spotify_credentials

    if client_id is None or client_secret is None:
        pytest.fail("One of those keys are empty!")
    
    assert client_id is not None and client_secret is not None, "The key is set!"

def test_connection_with_spotify_api(spotify_credentials):

    client_id, client_secret = spotify_credentials

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
    result = sp.search(q='Iron Maiden', type='artist')

    if result is None:
        pytest.fail("Look the connection with Spotify")

    assert result is not None