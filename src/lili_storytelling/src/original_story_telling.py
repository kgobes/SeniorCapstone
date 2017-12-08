#!/usr/bin/env python

import time
import rospy
import test_story
import cinema_story
import pickle
from dialog import Dialog
from player import Player
from story import Story
from story_map import StoryMap
from lili_avatar import LILIAvatar

def test():
	rospy.init_node('story_telling')
	avatar = LILIAvatar()
	time.sleep(1)

	avatar.speak('Hi! My name is Lili. What is yours?')
	name = avatar.listen()

	#add Dictionary Map creation
	dict_map = StoryMap("Predefined Map")

	#player = Player(test_story.zoo_start, test_story.zoo_nodes, name)
	player = Player(cinema_story.cinema_start, cinema_story.cinema_nodes, name)
	
	#avatar.speak('Hi ' + name + ', nice to meet you.')

	#zoo_story = Story(player, test_story.zoo_start)
	movie_story = Story(player, cinema_story.cinema_start)
    
	f = open('pickleTest', 'w')
	#pickle.dump(zoo_story, f)
	pickle.dump(movie_story, f)
	f.close()

	f = open('pickleTest', 'r')
	newStory = pickle.load(f)
	f.close()

	newStory.walk(player, avatar)


if __name__ == '__main__':
	test()
