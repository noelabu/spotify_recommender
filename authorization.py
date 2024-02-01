import requests
import json
import base64

from decouple import config

class Authorization():

    def __init__(self):
        self.url = config('SPOTIFY_URL_TOKEN')
        self.client_id = config('SPOTIFY_CLIENT_ID')
        self.client_secret = config('SPOTIFY_CLIENT_SECRET')
        self.auth_header = base64.urlsafe_b64encode((self.client_id + ':' + self.client_secret).encode('ascii'))
        self.refresh_token = config('SPOTIFY_REFRESH_TOKEN')
    
    def refresh_token_auth(self):
        data = {
            "grant_type" : "refresh_token",
            "refresh_token": self.refresh_token
        }

        header= {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % self.auth_header.decode('ascii')
        }

        spotify_request = requests.post(self.url, headers= header,data=data)
        report = spotify_request.json()
        access_token = report['access_token']
        return access_token