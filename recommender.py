import requests
import json
import base64

from authorization import Authorization
from search import SpotifySearch

Auth = Authorization()
access_token = Auth.refresh_token_auth()
search = SpotifySearch()

class SpotifyRecommend():

    def __init__(self):
        self.url = "https://api.spotify.com/v1/recommendations"
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+access_token
        }
    
    def recommend_tracks(self, song, artist_id, track_id, genre):
        data = {
            'seed_artists' : artist_id,
            'seed_tracks' :  track_id,
            'seed_genres' : genre
        }

        spotify_playlist = requests.get(self.url, headers=self.headers, params=data)
        report = spotify_playlist.json()
        
        playlist = []
        searched_song = search.search_song_and_artist(song, artist_id)
        playlist.append(searched_song)
        items = report["tracks"]

        for i in range(10):
            song = {}
            song["name"] = items[i]["name"]
            song["artist"] = items[i]["artists"][0]["name"]
            song["preview_url"] = items[i]["preview_url"]
            song["external_urls"] = items[i]["external_urls"]["spotify"]
            song["img"] = items[i]["album"]["images"][0]["url"]
            playlist.append(song)
        
        return playlist