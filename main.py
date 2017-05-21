from media import Video, Person
import tmdbsimple as tmdb
import fresh_tomatoes
import wikipedia

tmdb.API_KEY = '65abd8a5a458bd5b2f1fa71446e60c32'	# Insert your API key here
PERSON = 'Ang Lee'	# Insert your person (actor, director, etc) here
movies = []

# Search tmdb for person
search = tmdb.Search()
search.person(query = PERSON)

if search.results:
	result = search.results[0]	# Selects first, most relevant result
	name = result['name']
	person = Person(name,
					'http://image.tmdb.org/t/p/w342' + result['profile_path'],
					wikipedia.summary(name).encode('utf-8'))	# Ecode in utf-8 for special characters or other languages
	associated_movies = result['known_for']		# Picks top movies associated with person

	for movie in associated_movies:
		if movie['media_type'] == 'movie':	# Excludes non-movie media like trailers
			title = movie['title']
			image = 'http://image.tmdb.org/t/p/w342' + movie['poster_path']

			trailer = None
			identity = tmdb.Movies(movie['id'])
			videos = identity.videos()['results']	# Acquires associated videos of selected movie

			if videos:
				for video in videos:
					
					if video['type'] == 'Trailer':	# Excludes non-trailer media like behind-the-scenes
						trailer = video['key']	# Acquires Youtube ID
						break	# Ensures that first, most relevant result is selected
					else:
						continue	# Skips video if not trailer
			
			if not trailer:
				continue	# Skips movie if no trailer found

			movies.append(Video(title, image, trailer))
	# Outputs formatted page
	fresh_tomatoes.open_movies_page(movies, person)
else:
	# If no results for search, output error page
	fresh_tomatoes.error_page()