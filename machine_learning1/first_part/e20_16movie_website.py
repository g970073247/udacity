import fresh_tomatoes
import e20_4media

toy_story = e20_4media.Movie('Toy Story',
						'A Story of a boy and his toys that come to life',
						'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
						'https://www.youtube.com/watch?v=vwyZH85NQC4')


avatar = e20_4media.Movie('Avatar',
						'A marine on an alien planet',
						'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
						'http://www.youtube.com/watch?v=-9ceBgWV8io')
'''
print avatar.storyline
#avatar.show_trailer()
print e20_4media.Movie.VALID_RATINGS
print e20_4media.Movie.__doc__
print e20_4media.Movie.__name__
print e20_4media.Movie.__module__
'''
avatar2 = e20_4media.Movie('Avatar2',
						'A marine on an alien planet',
						'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
						'http://www.youtube.com/watch?v=-9ceBgWV8io')

ratatouille = e20_4media.Movie('Ratatouille',
								'Storyline',
								'http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
								'heeps://www.youtube.com/watch?v=c3sBBRxDAqk')

monkey = e20_4media.Movie('Monkey Story','A story of a monkey to rescue his partners',
	'https://upload.wikimedia.org/wikipedia/zh/f/f1/Wu_Kong_Zhuan.jpg','http://video.mtime.com/66412/?mid=226435')

movies = [toy_story, avatar, avatar2, ratatouille, monkey]
fresh_tomatoes.open_movies_page(movies)


