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
entrance_text = ('Hello, welcome to the movie theater! If you would like to see the Superman showing at four, please proceed to the ticket booth to purchase your ticket.')

entrance_dialog = [Dialog(text=entrance_text, characterID=1)]

entrance = StoryNode('entrance', entrance_dialog, 'Node representing the entrance to the movie theatre.',
                     image_path='cinema_entrance.jpg')

#Below is needed when connecting two scenes
entrance_edge_text = ("Head to the movies")
entrance_edge_dialog = Dialog(text=entrance_edge_text)
entrance_edge = StoryEdge('head to the movies', entrance,dialog=entrance_edge_dialog)


### Ticket Counter ###
ticket_counter_edge_text = ('Here is your purchased ticket to see Superman. The movie showing will be in theater one.')

ticket_counter_edge_dialog = Dialog(text=ticket_counter_edge_text)

ticket_counter_node_dialog = [Dialog(text='Here is your purchased ticket. The movie will be showing in theater one.', characterID=1)]

ticket_counter_node = StoryNode('ticket counter', ticket_counter_node_dialog, 'Node representing the ticket counter.',
                        image_path='ticket_booth.jpg')

ticket_counter_edge = StoryEdge(' purchase a ticket', ticket_counter_node,
                        dialog=ticket_counter_edge_dialog)


### Candy Counter ###
candy_counter_edge_text = ('You walk into the lobby and the smell of buttered popcorn fills the air so you get in line at the concession counter.')

candy_counter_node_dialog = [Dialog(text='As you wait in line, the smell of popcorn grows stronger. Finally you get tothe front and buy a big bucket of popcorn.')]
#Dialog(text='Finally you get to the front and buy a big bucket of popcorn.')]
#, Dialog(text='You find a place to sit down and enjoy your popcorn.')]

candy_counter_node = StoryNode('candy counter', candy_counter_node_dialog, 'Node representing the concession stand.',
                        image_path='candy_counter.jpg')

candy_counter_edge = StoryEdge(' buy popcorn', candy_counter_node,
                        dialog=candy_counter_edge_text)


### Movie Screen ###
movie_screen_edge_dialog = Dialog(text='You walk into theater one. Please silence your cell phones, sit back, and enjoy the movie!.')

movie_screen_node_dialog = [Dialog(text='Please silence your cell phones, sit back, and enjoy the movie!')]

movie_screen_node = StoryNode('movie_screen', movie_screen_node_dialog, 'Node representing the movie screen.',
                         image_path='movie_screen.jpg')

movie_screen_edge = StoryEdge(' sit down in movie theater', movie_screen_node,
                         dialog=movie_screen_edge_dialog)


### Run into Friend ###
restroom_edge_dialog = Dialog(text='You go to the restroom and run into your friend Bob.')

restroom_node_dialog = [Dialog(text='Hello, funny seeing you here. I am excited to see Superman.', characterID=1)]

restroom_node = StoryNode('restroom',restroom_node_dialog, 'Node representing running into friend.',
		image_path='restroom.jpg')

restroom_edge = StoryEdge(' go to the restroom', restroom_node,
			dialog=restroom_edge_dialog)

### Exit ###
exit_edge_dialog = Dialog(text='You leave the movie theater.')

exit_node_text = ('We hope you enjoyed the movie! '
                  'Come again soon.')

exit_node_dialog = [Dialog(text=exit_node_text, characterID=1)]

exit_node = StoryNode('exit', exit_node_dialog,
                      'Node representing exiting the movie theater.')

exit_edge = StoryEdge(' leave the movie theater', exit_node,
                      dialog=exit_edge_dialog)


# For the Story construction:
cinema_nodes = [entrance, ticket_counter_node, candy_counter_node, 
	movie_screen_node, restroom_node, exit_node]
cinema_start = entrance
cinema_end = exit_node #Added

# Story Structure:

entrance.children = [ticket_counter_edge, exit_edge]

ticket_counter_node.children = [candy_counter_edge, movie_screen_edge, restroom_edge, exit_edge]

candy_counter_node.children = [movie_screen_edge, restroom_edge, exit_edge]

movie_screen_node.children = [candy_counter_edge, restroom_edge, exit_edge]

restroom_node.children = [candy_counter_edge, movie_screen_edge, exit_edge]

#exit_node.children = [test_story.entrance_edge]
