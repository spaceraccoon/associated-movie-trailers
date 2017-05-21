from media import Video, Person
import tmdbsimple as tmdb
import fresh_tomatoes
import wikipedia

tmdb.API_KEY = '65abd8a5a458bd5b2f1fa71446e60c32'	# Insert your API key here
PERSON = 'Ang Lee'	# Insert your person (actor, director, etc) here
movies = []

search = tmdb.Search()
search.person(query = PERSON)

if search.results:
	result = search.results[0]
	name = result['name']
	person = Person(name,
					'http://image.tmdb.org/t/p/w342' + result['profile_path'],
					wikipedia.summary(name).encode('utf-8'))	# Ecode in utf-8 for special characters or other languages
	associated_movies = result['known_for']

	for movie in associated_movies:
		if movie['media_type'] == 'movie':
			title = movie['title']

			image = 'http://image.tmdb.org/t/p/w342' + movie['poster_path']

			identity = tmdb.Movies(movie['id'])
			videos = identity.videos()['results']

			if videos:
				for video in videos:
					if video['type'] == 'Trailer':
						trailer = video['key']
						break
					else:
						continue
			else:
				continue

			movies.append(Video(title, image, trailer))
	fresh_tomatoes.open_movies_page(movies, person)
else:
	fresh_tomatoes.error_page()