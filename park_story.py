from story_node import StoryNode
from story_edge import StoryEdge
from dialog import Dialog

# StoryNode(self, name, description=None, dialog=None,
#                 children=None, image_path=None, auto=False)

# StoryEdge(self, key, child=None, dialog=None, weight=0)

# Story(self, player, root)

# Dialog(self, characterID=0, text=None, filepath=None)

Dialog.characterList = [None, "us2_mbrola"]

#NOTE : you need an "exit_node" named exactly so for every scene/story

#Movie Scene =============================================================
### Entrance ###
entrance_text = ('Hello, welcome to the park!')

entrance_dialog = [Dialog(text=entrance_text, characterID=1)]

entrance = StoryNode('entrance', entrance_dialog, 'Node representing the entrance to the park.',
                     image_path='park_entrance.jpg')

#Below is needed when connecting two scenes
entrance_edge_text = ("Head to the park")
entrance_edge_dialog = Dialog(text=entrance_edge_text)
entrance_edge = StoryEdge('head to park', entrance,dialog=entrance_edge_dialog)


### Feed Birds  ###
feed_birds_edge_text = ('Feed the pigeons with this bread.')

feed_birds_edge_dialog = Dialog(text=feed_birds_edge_text)

feed_birds_node_dialog = [Dialog(text='The birds flock to the bread.', characterID=1)]

feed_birds_node = StoryNode('feed birds', feed_birds_node_dialog, 'Node representing feeding birds.',
                        image_path='feed_birds.gif')

feed_birds_edge = StoryEdge(' feed the birds', feed_birds_node,
                        dialog=feed_birds_edge_dialog)


### Sit on Bench  ###
bench_edge_text = ('As you walk around the park, you find a bench to sit on')

bench_node_dialog = [Dialog(text='You sit on the bench and watch the people walk by')]

bench_node = StoryNode('bench', bench_node_dialog, 'Node representing sit on bench.',
                        image_path='bench.jpg')

bench_edge = StoryEdge(' sit on the bench', bench_node,
                        dialog=bench_edge_text)


### Swings ###
swings_edge_dialog = Dialog(text='You walk by the playground and sit on the swings.')

swings_node_dialog = [Dialog(text='You swing as you move your legs in and out!', characterID=1)]

swings_node = StoryNode('swings', swings_node_dialog, 'Node representing the swings.',
                         image_path='swings.jpg')

swings_edge = StoryEdge(' swing on the swings', swings_node,
                         dialog=swings_edge_dialog)


### Run into Friend ###
friend_edge_dialog = Dialog(text='You walk towards the pong and run into your friend Bob.')

friend_node_dialog = [Dialog(text='Hello, funny seeing you here. What a lovely day we are having.', characterID=1)]

friend_node = StoryNode('friend',friend_node_dialog, 'Node representing running into friend.',
		image_path='pond.jpg')

friend_edge = StoryEdge(' go to the pond', friend_node,
			dialog=friend_edge_dialog)

### Exit ###
exit_edge_dialog = Dialog(text='You leave the park.')

exit_node_text = ('You walk out of the park.')

exit_node_dialog = [Dialog(text=exit_node_text, characterID=1)]

exit_node = StoryNode('exit', exit_node_dialog,
                      'Node representing exiting the park.')

exit_edge = StoryEdge(' leave the park', exit_node,
                      dialog=exit_edge_dialog)


# For the Story construction:
park_nodes = [entrance, feed_birds_node, bench_node, 
	swings_node, friend_node, exit_node]
park_start = entrance
park_end = exit_node #Added

# Story Structure:

entrance.children = [feed_birds_edge, exit_edge]

feed_birds_node.children = [bench_edge, swings_edge, friend_edge, exit_edge]

bench_node.children = [swings_edge, friend_edge, exit_edge]

swings_node.children = [bench_edge, friend_edge, exit_edge]

friend_node.children = [bench_edge, swings_edge, exit_edge]

