import fresh_tomatoes
import movie
#Below shows you six movies's information
toy_story = movie.Movie('Toy Story',
						'A Story of a boy and his toys that come to life',
						'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
						'https://www.youtube.com/watch?v=vwyZH85NQC4')


avatar = movie.Movie('Avatar',
					 'A marine on an alien planet',
					 'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
					 'http://www.youtube.com/watch?v=-9ceBgWV8io')

cars_3 = movie.Movie('Cars_3',
					 'A story between two racers',
					 'https://upload.wikimedia.org/wikipedia/zh/9/9a/Cars_3.jpg',
					 'https://www.youtube.com/watch?v=IOANrDqUWx0&list=PL316wRwpvsnGtnh36mYWpxRyXnQ3y7GkU')

ratatouille = movie.Movie('Ratatouille',
						  'A story of mices cookings',
						  'http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
						  'https://www.youtube.com/watch?v=c3sBBRxDAqk')

monkey = movie.Movie('Monkey Story',
					'A story of a monkey to rescue his partners',
					'https://upload.wikimedia.org/wikipedia/zh/f/f1/Wu_Kong_Zhuan.jpg',
					'https://www.youtube.com/watch?v=yqk6Ch9NZ5I')


xmen = movie.Movie('X-Men: Days of Future',
	        		'A story of band of mutants',
	        		'https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg',
	        		'https://www.youtube.com/watch?v=gsjtg7m1MMM')

movies = [toy_story, avatar, cars_3, ratatouille, monkey, xmen]
fresh_tomatoes.open_movies_page(movies)


