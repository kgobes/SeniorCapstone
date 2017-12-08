from story_node import StoryNode
from story_edge import StoryEdge
from dialog import Dialog

# StoryNode(self, name, description=None, dialog=None,
#                 children=None, image_path=None, auto=False)

# StoryEdge(self, key, child=None, dialog=None, weight=0)

# Story(self, player, root)

# Dialog(self, characterID=0, text=None, filepath=None)

Dialog.characterList = [None, "us2_mbrola"]



#Movie Scene =============================================================
### Entrance ###
entrance_text = ('Hello, welcome to the movie theater! Please take your movie ticket and proceed to theater 1'
                 'We have an exciting movie for you today!')

entrance_dialog = [Dialog(text=entrance_text, characterID=1)]

entrance = StoryNode('entrance', entrance_dialog, 'Node representing the entrance to the movie theatre.',
                     image_path='cinema_images/cinema_entrance.jpg')


### Ticket Counter ###
ticket_counter_edge_text = ('You walk to the ticket counter. As you get close you see there is a showing for Superman at four. ')

ticker_counter_edge_dialog = Dialog(text=ticket_counter_edge_text)

ticket_counter_node_dialog = [Dialog(text='Hello, would you like to see Superman today? The ticket will be five dollars.', characterID=1)]

ticket_counter_node = StoryNode('ticket counter', ticket_counter_dialog, 'Node representing the ticket counter.',
                        image_path='cinema_images/ticket_booth.jpg')

ticket_counter_edge = StoryEdge('purchase a ticket', ticket_counter_node,
                        dialog=ticket_counter_edge_dialog)


### Candy Counter ###
candy_counter_edge_text = ('You walk into the lobby and the smell of buttered popcorn fills the air so you get in line at the concession counter.')

candy_counter_node_dialog = [Dialog(text='As you wait in line, the smell of popcorn grows stronger.'),
                      Dialog(text='Finally you get to the front and buy a big bucket of popcorn.'),
                      Dialog(text='You find a place to sit down and enjoy your sugary treat.')]

candy_counter_node = StoryNode('candy counter', candy_counter_node_dialog, 'Node representing the concession stand',
                        image_path='cinema_images/candy_counter.jpg')

candy_counter_edge = StoryEdge('buy popcorn', candy_counter_node,
                        dialog=candy_counter_edge_text)


### Movie Screen ###
movie_screen_edge_dialog = Dialog(text='You walk into theater one.')

movie_screen_node_dialog = [Dialog(text='Please silence your cell phones, sit back, and enjoy the movie!', characterID=1)]

movie_screen_node = StoryNode('movie_screen', movie_screen_node_dialog, 'Node representing the movie screen.',
                         auto=True, image_path='cinema_images/movie_screen.jpg')

movie_screen_edge = StoryEdge('sit down in movie theater', movie_screen_node,
                         dialog=movie_screen_edge_dialog)


### Run into Friend ###
restroom_edge_dialog = Dialog(text='You go to the restroom and run into your friend Bob.')

restroom_node_dialog = [Dialog(text='Hello, funny seeing you here. I am excited to see Superman.', characterID=1)]

restroom_node = StoryNode('restroom',restroom_node_dialog, 'Node representing running into friend.',
		image_path='cinema_images/restroom.jpg')

restroom_edge = StoryEdge('run into Bob', restroom_node,
			dialog=restroom_edge_dialog)

### Exit ###
exit_edge_dialog = Dialog(text='You leave the movie theater.')

exit_node_text = ('We hope you enjoyed the movie! '
                  'Come again soon.')

exit_node_dialog = [Dialog(text=exit_node_text, characterID=1)]

exit_node = StoryNode(None, exit_node_dialog,
                      'Node representing exiting the movie theater.')

exit_edge = StoryEdge('leave the movie theater', exit_node,
                      dialog=exit_edge_dialog)


# For the Story construction:
cinema_nodes = [entrance, ticket_counter_node, candy_counter_node, 
	movie_screen_node, restroom_node, exit_node]
cinema_start = entrance


# Story Structure:

entrance.children = [ticket_counter_edge, exit_edge]

ticket_counter_node.children = [candy_counter_edge, movie_screen_edge, restroom_edge, exit_edge]

candy_counter_node.children = [movie_screen_edge, restroom_edge, exit_edge]

movie_screen_node.children = [candy_counter_edge, restroom_edge, exit_edge]

restroom_node.children = [ticket_counter_edge, movie_screen_edge, restroom_edge, exit_edge]


