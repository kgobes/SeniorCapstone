from story_node import StoryNode
from story_edge import StoryEdge
import test_story
from dialog import Dialog

# StoryNode(self, name, description=None, dialog=None,
#                 children=None, image_path=None, auto=False)

# StoryEdge(self, key, child=None, dialog=None, weight=0)

# Story(self, player, root)

# Dialog(self, characterID=0, text=None, filepath=None)

Dialog.characterList = [None, "us2_mbrola"]


#Exit - used to exit entire store =============================================================
exit_edge_dialog = Dialog(text='You leave the story.')

exit_node_text = ('We hope you enjoyed the movie! '
                  'Come again soon.')

exit_node_dialog = [Dialog(text=exit_node_text, characterID=1)]

exit_node = StoryNode(None, exit_node_dialog,
                      'Node representing exiting the entire story.')

exit_edge = StoryEdge('leave the story',exit_node,dialog=exit_edge_dialog)


### Random node that can be inserted in story ==================
random_edge_dialog = Dialog(text = 'You run into your friend Bob')

#Try to insert the players name in 'random_node_text'
random_node_text = ('Hi, fancy seeing you here')

random_node_dialog = [Dialog(text=random_node_text, characterID=1)]

random_node = StoryNode('casually walking', random_node_dialog, 'Node representing randomly seeing your friend.')

random_edge = StoryEdge(' you are casually walking', random_node, dialog=random_edge_dialog)
