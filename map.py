from location import Location

class Map:
	'''
	This class represents the map for the story.
	It contains an array of locations that each have their own scenes to play within them. When the user create a story, they start with the map.
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
