class Media():
	def __init__(self, title, image):
		self.title = title
		self.poster_image_url = image

class Video(Media):
	def __init__(self, title, image, trailer):
		Media.__init__(self, title, image)
		self.trailer_youtube_url = trailer

class Person(Media):
	def __init__(self, title, image, bio):
		Media.__init__(self, title, image)
		self.bio = bio

class Video2(Media):
	def __init__(self, title, image, trailer):
		Media.__init__(self, title, image)
		self.trailer_youtube_url = trailer