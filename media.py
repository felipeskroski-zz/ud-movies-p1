# dependency used to open browser windows
import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # Class variable to define movie ratings
    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image, youtube_trailer):
        """Initiates the movie class.
        Attributes:
            title: the movie title
            storyline: a short plot of the movie
            poster_image: the poster image url
            youtube_trailer: the long youtube URL
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        """This opens the browser on the trailers youtube page"""
        webbrowser.open(self.youtube_trailer)
