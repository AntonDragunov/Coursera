class Vertex:
	
	def __init__(self):
		self._links = None
	
	@property
	def links(self):
		return self._links
	
	@links.setter
	def links(self, value):
		self._links = value


class Link:
	
	def __init__(self, v1, v2):
		self._v1 = v1
		self._v2 = v2
		self._dist = 1


class LinkedGraph:

	def __init__(self):
		self._links =