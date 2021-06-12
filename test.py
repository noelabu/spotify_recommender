
from authorization import Authorization
from search import SpotifySearch
from recommender import SpotifyRecommend

search = SpotifySearch()
recommender = SpotifyRecommend()

song = "Ride Home"
artist = "Ben & Ben"
genre = "opm"

track_id = search.search_tracks(song)
artist_id = search.search_artist(artist)

playlist = recommender.recommend_tracks(artist_id, track_id, genre)
print(playlist)
