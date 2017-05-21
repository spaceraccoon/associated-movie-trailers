class Media():
    def __init__(self, title, image):
        self.title = title
        self.poster_image_url = image


class Video(Media):
    """Video class for movies.

    Atributes:
        title (str): Title of movie.
        image (str): URL path to poster image.
        trailer (str): Youtube ID of trailer.

    """

    def __init__(self, title, image, trailer):
        Media.__init__(self, title, image)
        self.trailer_youtube_url = trailer


class Person(Media):
    """Person class for people.

    Atributes:
        title (str): Name of person.
        image (str): URL path to profile  image.
        bio (str): Bio of person.

    """
    def __init__(self, title, image, bio):
        Media.__init__(self, title, image)
        self.bio = bio
