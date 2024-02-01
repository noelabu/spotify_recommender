
#Import the libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for

import jinja2

from genre import genre
from authorization import Authorization
from search import SpotifySearch
from recommender import SpotifyRecommend

search = SpotifySearch()
recommender = SpotifyRecommend()

#Initializing the flask app
app = Flask(__name__) 
no_input = False 

#Routing of the page 
@app.route('/')
def home():
    return render_template('index.html', genres = genre, no_input=False)

@app.route('/no_input')
def no_input():
    return render_template('index.html', genres = genre, no_input=True)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():

    if request.method == "POST":

        artist = request.form.get('artist')
        track = request.form.get('track')
        genre = request.form.get('genre')

        if not track or not artist or not genre:
            return redirect(url_for("no_input"))
        else:

            artist_id = search.search_artist(artist)
            track_id = search.search_tracks(track)
            
            playlist = recommender.recommend_tracks(track, artist_id, track_id, genre)
            songs = [ song["name"] for song in playlist]
            artists = [ song["artist"] for song in playlist]

            return render_template('playlist.html', playlist=playlist)


#Run!
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)