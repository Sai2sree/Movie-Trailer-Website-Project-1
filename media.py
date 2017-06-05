# Create a data structure to store movie details
# Details include movie title, box art URL and a YouTube link to movie trailer


class Movie():
    '''
    This class 'Movie' stores the details of movie as mentioned below.
    The title of the movie is stored in 'title'.
    The url for poster of the movie is stored in 'poster_image_url'.
    The url for the trailer of the movie is stored in 'trailer_youtube_url'
    '''
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
