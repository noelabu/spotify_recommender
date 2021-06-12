import requests
import json
import base64

from authorization import Authorization

Auth = Authorization()
access_token = Auth.refresh_token_auth()

class SpotifySearch():

    def __init__(self):
        self.url = "https://api.spotify.com/v1/search"
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+access_token
        }
    
    def search_tracks(self, song_track):
        data = {
            'q' : song_track,
            'type': "track"
        }
        spotify_search = requests.get(self.url, headers=self.headers, params=data)
        report = spotify_search.json()

        items = report["tracks"]["items"][0]
        name = items["name"]
        id = items["id"]

        return id

        
    
    def search_artist(self, artist):
        data = {
            'q' : artist,
            'type': "artist"
        }
        spotify_search = requests.get(self.url, headers=self.headers, params=data)
        report = spotify_search.json()

        items = report["artists"]["items"][0]
        name = items["name"]
        id = items["id"]
        genres = ["genres"][:4]

        return id




