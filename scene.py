from story_node import StoryNode
from story import Story

class Scene:
	'''
	This class represents a scene in the story.
	It contains an array of 'story_nodes' that represent the exact nodes that can play within that scene.
	Ex: Scene: Movies Story_node: Buying a ticket
	'''

	def __init__(self, name, root):
		#: Name of the scene
		self.name = name	
		#: Story nodes that are within the scene, start with the root or starting node
		self.story_nodes = root 

	#add story_nodes by adding children to scenes starting from the root
