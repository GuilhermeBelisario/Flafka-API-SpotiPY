import pytest
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def client_id():
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    return client_id

@pytest.fixture
def client_secret():
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    return client_secret

