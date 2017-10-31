from scene import Scene
#import collections.abc.Sequence
#^ allows us to use Location[0] for example

class Location:
	'''
	This class represents a location in the story.
	It contains an array of 'scenes' that represent the class which holds related story_nodes that can play within the location.
	Ex: Location: City, Scene: Movies
	'''

	def __init__(self, name, list_of_scenes=None):
		#: Name of the location
		self.name = name	
		#: Scenes that are within the location, order of list doesnt matter because user decides the scenes
		self.list_of_scenes = {} # [] #list_of_scenes 
#		super().__init__()

		if list_of_scenes != None:	
			for key,val in list_of_scenes.items():
				if isinstance(val, Scene):
					self.list_of_scenes[key]=val
					#self.list_of_scenes.append(sce)
				else:
					utility_funcs.eprint(
						"Invalid Scene  passed to Location initializer!")



#	def __getitem__(self,i):
	
	def addScene(self, new_scene):
		self.list_of_scenes[new_scene.name] = new_scene

	def removeScene(self, rem_scene):
		del list_of_scene[rem_scene.name]
		#self.list_of_scenes.remove(rem_scene)

	def getScene(self, index):
		return list_of_scenes[index]
