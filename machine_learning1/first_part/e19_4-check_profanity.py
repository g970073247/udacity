def open_file():
	file = open('/home/wang/Desktop/udacity/first_part/movie_quotes/movie_quotes.txt')
	content_of_file = file.read()
	print content_of_file
	print "game over"
	file.close()
open_file()