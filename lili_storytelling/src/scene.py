#from story_node import StoryNode
#from story import Story

class Scene:
	'''
	This class represents a scene in the story.
	It contains an array of 'story_nodes' that represent the exact nodes that can play within that scene.
	Ex: Scene: Movies Story_node: Buying a ticket
	'''

	def __init__(self, name, root, start_edge, end, story_nodes):
		#: Name of the scene
		self.name = name	
		#: Story nodes that are within the scene, start with the root or starting node
		self.start = root
		self.start_edge = start_edge
		self.story_nodes = story_nodes
		#self.story_nodes = root 
		self.end = end
	#add story_nodes by adding children to scenes starting from the root
