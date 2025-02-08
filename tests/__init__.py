from dotenv import load_dotenv
from .connection_tests import test_client_id_and_client_secret_is_not_none
import os
import time

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if __name__ == "__main__":
    
    test_client_id_and_client_secret_is_not_none(client_id,client_secret)