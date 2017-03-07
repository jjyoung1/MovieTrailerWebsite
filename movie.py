import webbrowser

# Project: Udacity:Programming Foundations with Python:MovieTrailer
"""

"""
class Movie():
    """A model of a movie that meets the requirements of fresh_tomatoes.py"""
    def __init__(self, title, poster_image_url, trailer_url):
        """
        Constructor:
            Parameters: title, poster_image_url, trailer_url
            title: The title of the movie
             poster_image_url: A url to a image of the movie poster
             trailer_url: A url to a youtube video for the movie trailer
        """
        self.title = title
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = poster_image_url

    @classmethod
    def show_trailer(self):
        """
        Function: show_trailer()
            Description: Open up the trailer in a web browser
            Parameters: None
            Return Value: None
        """
        webbrowser.open(self.trailer_url)

