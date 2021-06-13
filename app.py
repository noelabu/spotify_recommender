
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

#Routing of the page 
@app.route('/')
def home():
    return render_template('index.html', genres = genre, no_input=False)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():

    if request.method == "POST":

        track = request.form.get('track')
        artist = request.form.get('artist')
        genre = request.form.get('genre')

        if not track or not artist or not genre:
            return redirect(url_for("home", no_input = True))
        else:

            track_id = search.search_tracks(track)
            artist_id = search.search_artist(artist)

            playlist = recommender.recommend_tracks(artist_id, track_id, genre)
            songs = [ song["name"] for song in playlist]
            artists = [ song["artist"] for song in playlist]

            return render_template('playlist.html', playlist=playlist)


#Run!
if __name__ == "__main__":
    app.run()