import webbrowser

#created class Movie
class Movie():
    """This class provides a way to store movie related info."""
    #VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #define init funtcion to intialize tilte of movie, storyline, poster image, youtube trailer
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #new method to show trailer  
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
   
