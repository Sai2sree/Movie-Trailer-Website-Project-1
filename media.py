# Create a data structure to store movie details
# Details include movie title, box art URL and a YouTube link to movie trailer


class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
