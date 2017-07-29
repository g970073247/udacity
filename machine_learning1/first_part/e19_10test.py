import urllib
def check_profanity():
	file = open('/home/wang/Desktop/udacity/first_part/movie_quotes/movie_quotes.txt')
	content_of_file = file.read()
	print content_of_file
	file.close()
	use_website(content_of_file)
	print '1'
	

def use_website(text_to_check):
	connetcion = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot")
	output = connetcion.read()
	print(output)
	connetcion.close()

check_profanity()
