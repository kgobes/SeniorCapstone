from location import Location
import utility_funcs
#from _collections_abc import Sequence

class StoryMap:
	'''
	This class represents the map for the story.

	'''

	def __init__(self, name, numscenes, numplayers, locations=None):
		self.name = name
		self.numscenes = numscenes
		self.numplayers = numplayers
		self.locations = {} #locations # location
#		super().__init__()

		if locations != None:	
			for key,val in locations.items():
				if isinstance(val, Location):
					self.locations[key]=val
					#self.locations.append(loc)
				else:
					utility_funcs.eprint(
						"Invalid Location passed to StoryMap initializer!")

#	def __getitem__(self,i):
#		return self.locations[i]
#	def __len__(self):
#		return len(self.locations)
#def __init__(self):
	#print("story created")
	
	#def addLocation(self, loc):
	#	(self.locations).append(loc)

	def setLocation(locationX):
		location = locationX
       	
	def setNumScenes(numscenesX):
       		numscenes = numscenesX
	def setNumPlayers(numplayersX):
		numplayers = numplayersX
	#for testing, take in location in hashmap
	def printStoryInfo(self, loc):
		print("name: "+ `self.name`+"\n number of scenes:"+`self.numscenes`
			+" number of players:"+`self.numplayers`+" location:"+`self.locations[loc].name`)
	#for testing, doesn't return desired data type yet
	def getName(self):
		return self.name
'''
	def __init__(self, name, list_of_locations, startNode, endNode):
		#: Name of the scene
		self.name = name	
		#: Locations available within the map
		self.list_of_locations = list_of_locations
		# All of the below are story_node objects - smallest unit of story / what LILI uses
		#: Node to start the story
		self.startNode = startNode
		#: Node to end the story
		self.endNode = endNode
		#: Keep track of current node in the map, start at start node
		self.currNode = startNode

	
	def addLocation(self, new_location):
		self.list_of_locations.append(new_location)

	def removeLocation(self, rem_location):
		self.list_of_locations.remove(rem_location) 

	def setCurrNode(self, currNode):
		self.currNode = currNode

	def changeStartNode(self, newStartNode):
		self.startNode = newStartNode

	def changeEndNode(self, newEndNode):
		self.endNode = newEndNode
'''
