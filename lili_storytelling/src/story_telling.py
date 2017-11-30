#!/usr/bin/env python

import sys
from story_map import StoryMap
from location import Location
#import ExtendedQLabel
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#file with the test() that runs the whole Lili
#from story_telling import test
from dict_map import dictMap
import os
import pickle
#from story_telling import test

#imports for test() from story_telling
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
import global_nodes
import testSpeakerRecog

#app is main application- our platform for interaction with the user
app = QApplication(sys.argv)

#declarations for all windows needed: 
#start screen
#choose new or edit existing
startScreen = QWidget()
startScreen.resize(900, 600)
p = startScreen.palette()
p.setColor(startScreen.backgroundRole(), Qt.black)
startScreen.setPalette(p)
#Choose location- select where they want the story to take place
chooseLocScreen = QWidget()
chooseLocScreen.resize(900, 600)
#choose scene and player settings (num scenes, num players)
sceneSettingsScreen = QWidget()
sceneSettingsScreen.resize(900, 600)
p = sceneSettingsScreen.palette()
p.setColor(sceneSettingsScreen.backgroundRole(), Qt.black)
sceneSettingsScreen.setPalette(p)
#activity specifics screen- choose activity and randomness level
activityScreen = QWidget() #screen repeated for each scene
activityScreen.resize(900, 600)
#chose the story to play 
chooseStoryPlayScreen = QWidget()
chooseStoryPlayScreen.resize(900, 600)
#Add player voice
addPlayerScreen = QWidget()
addPlayerScreen.resize(900,600)



#how many scenes there are; counts down; arbitrary number initially to test changing it
numscene = 8
numscenesBox = None
numplayersBox = None
#location chosen on chooose Loc screen
locationChosen = None
#used to turn button off during location selection
lastButtonClicked = None
#number of players chosen
numberOfPlayers = 0
activitySelect = QComboBox(activityScreen)


'''
window = QWidget()
window.show()
layout = QGridLayout(window)
layout.addWidget(activityScreen)
#layout.addWidget(startScreen)
#layout.addWidget(chooseLocScreen)
#layout.addWidget(sceneSettingsScreen)
'''

def main():
	#Start the app
	#preload the scenes from function of another class
#	window.resize(900, 600)
	#dict_map.createMap()
	mainMenu()
	#dict_map.createMap()
	

def chooseLocation():	
	title = QLabel('Select a Location for Your Story', chooseLocScreen)
	title.setStyleSheet("font: bold 15pt")
	title.move(320,30)

	story_name_label = QLabel("Story Name:", chooseLocScreen)
	story_name_label.move(320,60)
	global story_name
	story_name = QLineEdit(chooseLocScreen)
	story_name.move(420,60)

	choose = QPushButton("Choose this location", chooseLocScreen)
	choose.setEnabled(False)
#       QCoreApplication::processEvents()                                                                                          
        choose.clicked.connect(chooseSceneSettings)
        choose.move(375,550)
	global lastButtonClicked
	lastButtonClicked = choose

	loc1 = QLabel(chooseLocScreen)
	loc1.setGeometry(100,100,200,150)
	loc1.setPixmap(QPixmap('locimages/city.jpg'))
	loc1Text = QPushButton("City", chooseLocScreen)
	loc1Text.setGeometry(160,260,100,25)
	loc1Text.setStyleSheet("background-color: white")
	loc1Text.clicked.connect(lambda: locationSelect(loc1Text, "City", choose))

	loc2 = QLabel(chooseLocScreen)
	loc2.setGeometry(350,100,200,150)
	loc2.setPixmap(QPixmap('locimages/mountains.jpg'))
	loc2Text = QPushButton("Mountains", chooseLocScreen)
        loc2Text.setStyleSheet("background-color: white")
        loc2Text.clicked.connect(lambda: locationSelect(loc2Text, "Mountain", choose))
	loc2Text.setGeometry(400,260,100,25)

	loc3 = QLabel(chooseLocScreen)
	loc3.setGeometry(600,100,200,150)
	loc3.setPixmap(QPixmap('locimages/forest.jpg'))
	loc3Text = QPushButton("Forest", chooseLocScreen)
	loc3Text.setStyleSheet("background-color: white")
        loc3Text.clicked.connect(lambda: locationSelect(loc3Text, "Forest", choose))
       	loc3Text.setGeometry(650,260,100,25)


	loc4 = QLabel(chooseLocScreen)
	loc4.setGeometry(100,320,200,150)
	loc4.setPixmap(QPixmap('locimages/ocean.jpg'))
	loc4Text = QPushButton("Ocean", chooseLocScreen)
	loc4Text.setStyleSheet("background-color: white")
        loc4Text.clicked.connect(lambda: locationSelect(loc4Text, "Ocean", choose))
       	loc4Text.setGeometry(150,480,100,25)


	loc5 = QLabel(chooseLocScreen)
	loc5.setGeometry(350,320,200,150)
	loc5.setPixmap(QPixmap('locimages/farm.jpg'))
	loc5Text = QPushButton("Farm", chooseLocScreen)
	loc5Text.setStyleSheet("background-color: white")
        loc5Text.clicked.connect(lambda: locationSelect(loc5Text, "Farm", choose))
       	loc5Text.setGeometry(410,480,100,25)

	loc6 = QLabel(chooseLocScreen)
	loc6.setGeometry(600,320,200,150)
	loc6.setPixmap(QPixmap('locimages/desert.jpg'))
	loc6Text = QPushButton("Desert", chooseLocScreen)
	loc6Text.setStyleSheet("background-color: white")
        loc6Text.clicked.connect(lambda: locationSelect(loc6Text, "Desert", choose))
       	loc6Text.setGeometry(650,480,100,25)

#	global numscenesBox	
#	print(numscenesBox.currentText())
#	global numscene
#	numscene = int(str(numscenesBox.currentText()))

	chooseLocScreen.show()


#method to read user input for choosing location 
def locationSelect(clickedButton, buttonName, choose):
	#if the button hasn't been selected yet; it is white now
	if(clickedButton.palette().button().color().name() == "#ffffff"): #color white
		#change color of button
		clickedButton.setStyleSheet("background-color: skyblue")
		global locationChosen
		#set new location
		locationChosen = buttonName
		print("my location is: ", locationChosen)
		#allow user to move on from this screen
		choose.setEnabled(True)
		#change the color of last button clicked
		global lastButtonClicked	
		lastButtonClicked.setStyleSheet("background-color: white");
		lastButtonClicked = clickedButton
	else:
		#if the color is not white and it is clicked, make it white
		clickedButton.setStyleSheet("background-color: white")
		locationChosen = None
		print("my location is: ", locationChosen)
		#user can't change screens until they choose another location
		choose.setEnabled(False)

		
def chooseSceneSettings():
	global story_name
	global my_story_name
	my_story_name = story_name.text()
	my_story_name = str(my_story_name)
	startScreen.hide()
	title = QLabel('Choose Scene Settings', sceneSettingsScreen)
        title.setStyleSheet("color:white; font: bold 30pt")
        title.move(230,30)
	#choose num players
	numPlayerLabel  = QLabel("Number of players: ",sceneSettingsScreen)
        numPlayerLabel.setStyleSheet("color: white; font: bold 20pt")
        numPlayerLabel.move(250, 150)
	global numplayersBox
	numplayersBox = QComboBox(sceneSettingsScreen)
	numplayersBox.addItem("1", sceneSettingsScreen)
	numplayersBox.addItem("2", sceneSettingsScreen)
	numplayersBox.addItem("3",sceneSettingsScreen)
	numplayersBox.addItem("4",sceneSettingsScreen)
	numplayersBox.addItem("5",sceneSettingsScreen)
	numplayersBox.move(500, 145)
        numplayersBox.resize(80,40)
	#choose num scenes
	numSceneLabel  = QLabel("Number of scenes: ",sceneSettingsScreen)
	numSceneLabel.move(250, 230)
        numSceneLabel.setStyleSheet("color : white; font: bold 20pt")
	global numscenesBox
	numscenesBox = QComboBox(sceneSettingsScreen)
	numscenesBox.resize(80,40)
	#Ensure allowing number of scenes available
	loc = dictMap.locations[locationChosen]
	index = 1
	for sc in loc.list_of_scenes:
		numscenesBox.addItem(str(index),sceneSettingsScreen)
		index = index+1

#	numscenesBox.addItem("1",sceneSettingsScreen)
#	numscenesBox.addItem("2",sceneSettingsScreen)
#	numscenesBox.addItem("3",sceneSettingsScreen)
#	numscenesBox.addItem("4",sceneSettingsScreen)
#	numscenesBox.addItem("5",sceneSettingsScreen)
        numscenesBox.move(500, 225)
	#later add: select specfic players
	button = QPushButton("Done", sceneSettingsScreen)
	button.clicked.connect(getSceneNumChosen)	
	button.move(400, 350)
	button.resize(120,60)
	button.setStyleSheet("font: 20pt")
	chooseLocScreen.hide()
	sceneSettingsScreen.show()
#helper method for getting the number of scenes selected once button is pressed
def getSceneNumChosen():
	global numscene
        print(numscenesBox.currentText())
        numscene = int(str(numscenesBox.currentText()))
	global numplayers
	numplayers = int(str(numplayersBox.currentText()))
        print("Numscene within new helper method "+`numscene`)
	#create map object
	#create a new location
#	myMap = StoryMap("Kira's Sweet Story Map", numscene, numplayers, {locationChosen:dictMap.locations[locationChosen]})
#	myMap.printStoryInfo(locationChosen) #this doesn't work yet
	print("printing after that story shit printed")
	#need to format this correctly
	#print myMap.getName
#	print(myMap.getName())
	#myMap = map.Map()
	
#go to choose activities for scenes method
	chooseActivities()

def chooseActivities():
#	chooseLocScreen.hide()
	sceneSettingsScreen.hide()	
	#NEW
	#Create map to add to created maps
	global mymap
	#Create new location

	#Array of Scenes
	global chosen_scenes
	chosen_scenes = {}
	global first_scene
	first_scene = 0	
	#mymap = StoryMap("My Map", numscenes, 1, {locationChosen:dictMap.locations[locationChosen]})
	'''	
	if(numscene < 1):
		activityScreen.hide()
		mainMenu()	
	'''
	title = QLabel('Scene Activity Selection', activityScreen)
        title.setStyleSheet("font: bold 15pt")
        title.move(320,30)
	actLabel = QLabel('Choose an activity for Scene ', activityScreen)
	actLabel.update()
	global sceneNum
	sceneNum = QLabel('', activityScreen)
	sceneNum.setNum(numscene)
	actLabel.move(300, 100)
	sceneNum.move(500, 100)
	sceneNum.update()
	createActivityOptions()
	#activitySelect = QComboBox(activityScreen)
	#activitySelect.addItem("Treasure Hunting", activityScreen)
	#activitySelect.addItem("Hiking", activityScreen)
	global activitySelect
	activitySelect.move(420, 200)
	button = QPushButton("Done", activityScreen)
	#if(numscene>0):
		#numscene = numscene-1
		
	#print(numscene)
	button.clicked.connect(chooseActivitiesHelper)
	#button.move(350, 400)
	#activityScreen.show()
		#else:
		#button.clicked.connect(exit)
	        #button.clicked.connect()
#lambda: chooseActivitiesHelper(numscene)) 
       	button.move(350, 400)	
	#window.show()
#	activityScreen.show()
	'''
	if(numscene == 6):
		activityScreen.show()
	else:
		activityScreen.update()
	'''
	activityScreen.show()
	
def chooseActivitiesHelper():
	global numscene
	numscene -= 1
	global start_node
	global first_scene
	if(numscene < 0):
		activityScreen.hide()
		mainMenu()
	elif(numscene == 0): #Last scene
		print(numscene)
		print(activitySelect.currentText())
		sceneName = unicode(activitySelect.currentText())
		chosen_scenes[sceneName]=dictMap.locations[locationChosen].list_of_scenes[sceneName]
		activityScreen.hide()
		#global start_node
		#global first_scene
		if first_scene ==0: #Get name of first scene
			print("in if")
			#start_node = sceneName
			start_node = dictMap.locations[locationChosen].list_of_scenes[sceneName].start #passed the root story node for start
		#first_scene = first_scene +1	
		createMyMap()
	#	mainMenu()
	else:
		global sceneNum
		sceneNum.setNum(numscene)
		#Create scene array
		print(activitySelect.currentText())
		sceneName = unicode(activitySelect.currentText())
		chosen_scenes[sceneName]=dictMap.locations[locationChosen].list_of_scenes[sceneName]
		#global start_node
		#start_node = None
		#global start_node
		#global first_scene
		if first_scene ==0: #Get name of first scene
			print("in if")
			#start_node = sceneName
			start_node = dictMap.locations[locationChosen].list_of_scenes[sceneName].start #passed the root story node for start
		first_scene = first_scene +1	
		print(numscene)
		print(activitySelect.currentText())


def createMyMap():
	chosenLocationObject = Location(locationChosen,chosen_scenes);
	#Find startNode given first_scene
	#start_node = dictMap.locations[locationChosen].list_of_scenes[first_scene].story_nodes #passed the root story node for start
	print(my_story_name)
	myMap = StoryMap(my_story_name, numscene, numplayers, {locationChosen:chosenLocationObject})
	#start_node = dictMap.locations[locationChosen].list_of_scenes["Movies"].story_nodes #passed the root story node for start
	global start_node
	myMap.startNode = start_node
	print(myMap.startNode.name)
	#Write map to a file
	arr_of_story_nodes = []
#	myMap.printStoryInfo(locationChosen) #this doesn't work yet
	for keys,val in myMap.locations[locationChosen].list_of_scenes.items():
		for key,scene in myMap.locations[locationChosen].list_of_scenes.items():
			#append start node of scenes to this 
			if key != keys:
				myMap.locations[locationChosen].list_of_scenes[keys].end.children.append(myMap.locations[locationChosen].list_of_scenes[key].start_edge)
				#val.end.children.append(scene.start)
				
	#			myMap.locations[locationChosen].list_of_scenes[keys].end.children= [test_story.entrance_edge]
			#	print(myMap.locations[locationChosen].list_of_scenes[keys].end.children.key)
				arr_of_story_nodes.extend(val.story_nodes) 
		print(keys)	
		myMap.locations[locationChosen].list_of_scenes[keys].end.children.append(global_nodes.exit_edge)
	#Link stories together by connecting their "exit_node" and "entrance"
	player = Player(myMap.startNode, arr_of_story_nodes, myMap.name)
	my_story = Story(player, myMap.startNode)
	#f = open('~/catkin_ws/src/lili_storytelling/src/createdStories','w')
	f = open('createdStories','a')
	pickle.dump(my_story, f)
	f.close()
	startScreen.show()
	mainMenu()


#method to add specific scene activity choices for each location
def createActivityOptions():
	global activitySelect
	activitySelect.clear()
	for key in (dictMap.locations[locationChosen]).list_of_scenes.keys():
		activitySelect.addItem(key,activityScreen)
		#activitySelect.addItem(sce.name, activityScreen)

#	if(locationChosen == "city"):
#		activitySelect.addItem("Movies", activityScreen)
#		activitySelect.addItem("Museum", activityScreen)
#	else:
#		activitySelect.addItem("Treasure Hunting", activityScreen)
#		activitySelect.addItem("Hiking", activityScreen)


	
		
def chooseStoryToPlay():
	startScreen.hide()
	story_to_play = QLabel("Story to Play: ",chooseStoryPlayScreen)
        story_to_play.move(290, 200)
	global stories
	stories = {}
	num_stories = 0
	cwd = os.getcwd()
#	filename = cwd + "/createdStories"
	global storyToPlayBox
	storyToPlayBox = QComboBox(chooseStoryPlayScreen)
	f = open('createdStories','r')
	while True:
		try:
			story = pickle.load(f)
			stories[story.player.name] = story	
			#print(story.player.name)
			#stories.append(pickle.load(f))
		except EOFError:
			break
		num_stories = num_stories + 1
	f.close()
	#global storyToPlayBox
	#storyToPlayBox = QComboBox(chooseStoryPlayScreen)
	for story in stories:
		storyToPlayBox.addItem(story, chooseStoryPlayScreen)
	storyToPlayBox.move(410, 200)
	button = QPushButton("Play", chooseStoryPlayScreen)
	button.clicked.connect(playStory)	
	button.move(350, 250)
	back_button = QPushButton("Main Menu", chooseStoryPlayScreen)
	back_button.clicked.connect(playStoryToMainMenu)
	back_button.move(450,250)
	chooseStoryPlayScreen.show()

def playStory():
	global stories
	storyName = unicode(storyToPlayBox.currentText())
	print(storyName)
	story = stories[storyName]
#	story.printStory()
	#for key in story.player.completed:
	#	print(key)
	rospy.init_node('story_telling')
	avatar = LILIAvatar()
	time.sleep(1)
	avatar.speak('Hi! My name is Lili. What is yours?')
	name = avatar.listen()
	#for speaker recognition think about creating player here after name
	#register players
	story.walk(story.player,avatar)


def playStoryToMainMenu():
	#chooseStoryPlayScreen.hide()
	chooseStoryPlayScreen.close()
	startScreen.show()
	mainMenu()

def enrollSpeakerSetup():
	title = QLabel('Add a New Player', addPlayerScreen)
	title.setStyleSheet("font: bold 15pt")
	title.move(320, 30)
	player_name_label = QLabel("Enter Name: ", addPlayerScreen)
	player_name_label.move(270, 90)
	global player_name_q
	player_name_q = QLineEdit(addPlayerScreen)
	player_name_q.move(370, 90) 
	instructions = QLabel("Click record and say the following instructions to add a new player's voice to the system", addPlayerScreen)
	instructions.move(180,150)
	repeat_words = QLabel("One fish, two fish, red fish, blue fish. \nBlack fish, blue fish, old fish, new fish. \nThis one has a little star.\nThis one has a little car.", addPlayerScreen)
	repeat_words.move(280,200)	
	record = QPushButton('Record', addPlayerScreen)
	record.move(310, 300)
	record.clicked.connect(enrollSpeakerCall)
	back = QPushButton('Main Menu', addPlayerScreen)
	back.move(420,300)
	back.clicked.connect(enrollToMainMenu)
	global record_text
	record_text = QLabel('						',addPlayerScreen)
	record_text.move(320,330)
	startScreen.hide()
	addPlayerScreen.show()

def enrollSpeakerCall():
	global player_name_q
	player_name = str(player_name_q.text())
	record_text.setText("Recording...")
	record_text.repaint()
	print("Player name is ")
	print(player_name)
	print(os.getcwd())
	valid = testSpeakerRecog.enrollSpeaker(player_name)
	#record_text.setText("Recording...")
	if valid == 1:
		record_text.setText("Error recording, please click record again")
	else:
		record_text.setText("Done recording")
		

def enrollToMainMenu():
	addPlayerScreen.hide()
	startScreen.show()
	

def mainMenu():
#	window.hide()
	title = QLabel('Main Menu', startScreen)
        title.setStyleSheet("color: white; font: bold 20pt")
	#title.setStyleSheet("color:white")
        title.move(320,30)
	#button for creating new story or editing old
	createEdit = QPushButton("Create or Edit Story", startScreen)
	createEdit.resize(200,70)
	createEdit.clicked.connect(chooseLocation)
	createEdit.move(300, 150)
	#button for playing existing
	playExisting = QPushButton("Play Existing Story", startScreen)
	playExisting.resize(200,70)
#	playExisting.clicked.connect(exit) #eventually will have list of stories and then play them

	#UNCOMMENT WHEN USING STORY_TELLING.PY AGAIN
	#playExisting.clicked.connect(test) #eventually will have list of stories and then play them
	playExisting.clicked.connect(chooseStoryToPlay)
	playExisting.move(300, 250)

	#button for speech recognition 
	addPlayers = QPushButton("Add Players", startScreen)
	addPlayers.resize(200,70)
	addPlayers.clicked.connect(enrollSpeakerSetup) #will go into speech recognition mode
	addPlayers.move(300, 350)
	#Try comething 
	startScreen.show()
	app.exec_()
#chooseLocation()
#chooseSceneSettings()
#main()





def test():
	#rospy.init_node('story_telling')
	avatar = LILIAvatar()
	time.sleep(1)

	avatar.speak('Hi! My name is Lili. What is yours?')
	name = avatar.listen()

	#add Dictionary Map creation
	#dict_map = StoryMap("Predefined Map")

	#player = Player(test_story.zoo_start, test_story.zoo_nodes, name)
	player = Player(cinema_story.cinema_start, cinema_story.cinema_nodes, name)
	
	#avatar.speak('Hi ' + name + ', nice to meet you.')

	#======== DYNAMIC FUNCTIONALITY to be implemented ====
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
	mapGUI.main()



mainMenu()
#if __name__ == '__main__':
#main()
