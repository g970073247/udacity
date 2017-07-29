import fresh_tomatoes
import e20_4media

toy_story = e20_4media.Movie('Toy Story',
						'A Story of a boy and his toys that come to life',
						'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
						'https://www.youtube.com/watch?v=vwyZH85NQC4')

#print toy_story.storyline
#toy_story.show_trailer()

avatar = e20_4media.Movie('Avatar',
						'A marine on an alien planet',
						'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
						'http://www.youtube.com/watch?v=-9ceBgWV8io')

#print avatar.storyline
#avatar.show_trailer()

print e20_4media.Movie.VALID_RATINGS
print e20_4media.Movie.__doc__
print e20_4media.Movie.__name__
print e20_4media.Movie.__module__
monkey = e20_4media.Movie('Monkey Story','A story of a monkey to rescue his partners',
	'https://upload.wikimedia.org/wikipedia/zh/f/f1/Wu_Kong_Zhuan.jpg','http://video.mtime.com/66412/?mid=226435') 
#print monkey.storyline
#monkey.show_trailer()
