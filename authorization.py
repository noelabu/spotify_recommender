import requests
import json
import base64

class Authorization():

    def __init__(self):
        self.url = "https://accounts.spotify.com/api/token"
        self.client_id = "de83c9b1a975453093613f4b131d8255"
        self.client_secret = "191725626ab040958700c96d43fc164f"
        self.auth_header = base64.urlsafe_b64encode((self.client_id + ':' + self.client_secret).encode('ascii'))
        self.refresh_token = 'AQDlcGE1D5BbZYPo9qYwqDwbnTSIyPqjjzLSpgHw-nOFzam8uNlsIcgiA-5LilTB0rUUZD9_TRlE6NQq6h2bUbTNS5ApnlfrRedwkTDi9F6PlYllNAerlUj33byrqO_hKDk'
    
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