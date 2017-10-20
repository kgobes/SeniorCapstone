from scene import Scene

class Location:
	'''
	This class represents a location in the story.
	It contains an array of 'scenes' that represent the class which holds related story_nodes that can play within the location.
	Ex: Location: City, Scene: Movies
	'''

	def __init__(self, name, list_of_scenes):
		#: Name of the location
		self.name = name	
		#: Scenes that are within the location, order of list doesnt matter because user decides the scenes
		self.list_of_scenes = list_of_scenes


	def addScene(self, new_scene):
		self.list_of_scenes.append(new_scene)

	def removeScene(self, rem_scene):
		self.list_of_scenes.remove(rem_scene)

