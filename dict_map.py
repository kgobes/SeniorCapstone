
from story_node import StoryNode
from scene import Scene
from location import Location
from story_map import StoryMap
import test_story
import cinema_story
import park_story

'''
	This file creates the map that holds the values the GUI 
	needs in order to display choices to the user of which
	scene/location are available. It also associates a set of
	story nodes to one scene
'''

#def createMap():
	#Scene 1 - Movie scene - story nodes within "cinema_story.py"
movies = Scene('Movies', cinema_story.entrance,cinema_story.entrance_edge, cinema_story.exit_node, cinema_story.cinema_nodes)
#scene2 = Scene('Park', 0, 0, [])
zoo = Scene('Zoo',test_story.entrance,test_story.entrance_edge,test_story.exit_node, test_story.zoo_nodes)
park = Scene('Park', park_story.entrance, park_story.entrance_edge, park_story.exit_node, park_story.park_nodes)

	#Location 1 - City - only has one scene right now
movie_scenes_list = {movies.name:movies,zoo.name:zoo, park.name:park}
location1 = Location("City",movie_scenes_list)


	#Map that holds all the possible data to play
number_of_scenes = len(location1.list_of_scenes)
number_of_players = 1
	#locations = [location1] #Must maintain a list of possible locations
locations = {"City": location1}
global dictMap
dictMap = StoryMap("Dictionary Map", number_of_scenes, number_of_players,locations)	
	#dictMap.addLocation(location1)	


#Array of maps created by the users
# -further implementation should allow user to play these maps
global created_maps
created_maps = []

'''
def main():
	createMap()
	print(`dictMap.name`)
	print(`dictMap.locations["City"].list_of_scenes[0].name`)
	#print `((dictMap.location[0]).getScene(0)).name`

main()

'''


		


