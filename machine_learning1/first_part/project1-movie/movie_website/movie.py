import webbrowser


class Movie():
	'''This class provides a way to store movie related informations'''
# __init__ function is used to initialize the class,it needs you to input four arguments:movie_title, movie_storyline, poster_image, trailer
	def __init__(self, movie_title, movie_storyline, poster_image, trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer

# This function to show the trailer of movie
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		
