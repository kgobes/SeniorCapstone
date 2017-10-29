import sys
import map
#import ExtendedQLabel
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

#app is main application- our platform for interaction with the user
app = QApplication(sys.argv)

#declarations for all windows needed: 
#start screen
#choose new or edit existing
startScreen = QWidget()
startScreen.resize(900, 600)
#Choose location- select where they want the story to take place
chooseLocScreen = QWidget()
chooseLocScreen.resize(900, 600)
#choose scene and player settings (num scenes, num players)
sceneSettingsScreen = QWidget()
sceneSettingsScreen.resize(900, 600)
#activity specifics screen- choose activity and randomness level
activityScreen = QWidget() #screen repeated for each scene
activityScreen.resize(900, 600)

numscene = 8
#location chosen on chooose Loc screen
locationChosen = None
#used to turn button off during location selection
lastButtonClicked = None
#number of players chosen
numberOfPlayers = 0
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
	mainMenu()
	print('hey')
#	chooseLocation()

def chooseLocation():	
	title = QLabel('Select a Location for Scene 1', chooseLocScreen)
	title.setStyleSheet("font: bold 15pt")
	title.move(320,30)

	choose = QPushButton("Choose this location", chooseLocScreen)
	choose.setEnabled(False)
#       QCoreApplication::processEvents()                                                                                          
        choose.clicked.connect(chooseActivities)
        choose.move(375,550)
	global lastButtonClicked
	lastButtonClicked = choose
	
	loc1 = QLabel(chooseLocScreen)
	loc1.setGeometry(100,100,200,150)
	loc1.setPixmap(QPixmap('locimages/city.jpg'))
	loc1Text = QPushButton("City", chooseLocScreen)
	loc1Text.setGeometry(160,260,100,25)
	loc1Text.setStyleSheet("background-color: white")
	loc1Text.clicked.connect(lambda: locationSelect(loc1Text, "city", choose))

	loc2 = QLabel(chooseLocScreen)
	loc2.setGeometry(350,100,200,150)
	loc2.setPixmap(QPixmap('locimages/mountains.jpg'))
	loc2Text = QPushButton("Mountains", chooseLocScreen)
        loc2Text.setStyleSheet("background-color: white")
        loc2Text.clicked.connect(lambda: locationSelect(loc2Text, "mountain", choose))
	loc2Text.setGeometry(400,260,100,25)

	loc3 = QLabel(chooseLocScreen)
	loc3.setGeometry(600,100,200,150)
	loc3.setPixmap(QPixmap('locimages/forest.jpg'))
	loc3Text = QPushButton("Forest", chooseLocScreen)
	loc3Text.setStyleSheet("background-color: white")
        loc3Text.clicked.connect(lambda: locationSelect(loc3Text, "forest", choose))
       	loc3Text.setGeometry(650,260,100,25)


	loc4 = QLabel(chooseLocScreen)
	loc4.setGeometry(100,320,200,150)
	loc4.setPixmap(QPixmap('locimages/ocean.jpg'))
	loc4Text = QPushButton("Ocean", chooseLocScreen)
	loc4Text.setStyleSheet("background-color: white")
        loc4Text.clicked.connect(lambda: locationSelect(loc4Text, "ocean", choose))
       	loc4Text.setGeometry(150,480,100,25)


	loc5 = QLabel(chooseLocScreen)
	loc5.setGeometry(350,320,200,150)
	loc5.setPixmap(QPixmap('locimages/farm.jpg'))
	loc5Text = QPushButton("Farm", chooseLocScreen)
	loc5Text.setStyleSheet("background-color: white")
        loc5Text.clicked.connect(lambda: locationSelect(loc5Text, "farm", choose))
       	loc5Text.setGeometry(410,480,100,25)

	loc6 = QLabel(chooseLocScreen)
	loc6.setGeometry(600,320,200,150)
	loc6.setPixmap(QPixmap('locimages/desert.jpg'))
	loc6Text = QPushButton("Desert", chooseLocScreen)
	loc6Text.setStyleSheet("background-color: white")
        loc6Text.clicked.connect(lambda: locationSelect(loc6Text, "desert", choose))
       	loc6Text.setGeometry(650,480,100,25)

	global numscenes	
	print(numscenes.currentText())
	global numscene
	numscene = int(str(numscenes.currentText()))

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
	startScreen.hide()
	title = QLabel('Choose Scene Settings', sceneSettingsScreen)
        title.setStyleSheet("font: bold 15pt")
        title.move(320,30)
	#choose num players
	numPlayerLabel  = QLabel("Number of players: ",sceneSettingsScreen)
        numPlayerLabel.move(290, 100)
	numplayers = QComboBox(sceneSettingsScreen)
	numplayers.addItem("1", sceneSettingsScreen)
	numplayers.addItem("2", sceneSettingsScreen)
	numplayers.addItem("3",sceneSettingsScreen)
	numplayers.addItem("4",sceneSettingsScreen)
	numplayers.addItem("5",sceneSettingsScreen)
	numplayers.move(410, 95)
        #choose num scenes
	numSceneLabel  = QLabel("Number of scenes: ",sceneSettingsScreen)
	numSceneLabel.move(290, 150)
	global numscenes
	numscenes = QComboBox(sceneSettingsScreen)
	numscenes.addItem("1",sceneSettingsScreen)
	numscenes.addItem("2",sceneSettingsScreen)
	numscenes.addItem("3",sceneSettingsScreen)
	numscenes.addItem("4",sceneSettingsScreen)
	numscenes.addItem("5",sceneSettingsScreen)
        numscenes.move(410, 145)
	#later add: select specfic players
	button = QPushButton("Done", sceneSettingsScreen)
	global numscene
	print(numscenes.currentText())
#	numscene = int(str(numscenes.currentText()))
	print("Numscene within choose scene setting"+`numscene`)
	button.clicked.connect(chooseLocation)	
	button.move(350, 400)
	
	#declaration of map object for this instance
	#myMap = 

	sceneSettingsScreen.show()


def chooseActivities():
	chooseLocScreen.hide()

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
	global activitySelect
	activitySelect = QComboBox(activityScreen)
	activitySelect.addItem("Treasure Hunting", activityScreen)
	activitySelect.addItem("Hiking", activityScreen)
	activitySelect.move(420, 200)
	button = QPushButton("Done", activityScreen)
	#if(numscene>0):
		#numscene = numscene-1
		
	print(numscene)
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
	if(numscene < 1):
		activityScreen.hide()
		mainMenu()
	else:
		print(numscene)
		print(activitySelect.currentText())
		#Saving the choices for scenes
		global sceneNum
		sceneNum.setNum(numscene)
	#	sceneNum.update()
	#	chooseActivities()
	'''
	numscene = numscene-1
	if(numscene>0):
		print("numscene is"+`numscene`)
		chooseActivities(numscene)
	#else:
		#done picking scenes
	'''

def mainMenu():
#	window.hide()
	title = QLabel('Main Menu', startScreen)
        title.setStyleSheet("font: bold 15pt")
        title.move(320,30)
	#button for creating new story or editing old
	createEdit = QPushButton("Create or Edit Story", startScreen)
	createEdit.clicked.connect(chooseSceneSettings)
	createEdit.move(375, 150)
	#button for playing existing
	playExisting = QPushButton("Play Existing Story", startScreen)
	playExisting.clicked.connect(exit) #eventually will have list of stories and then play them
	playExisting.move(375, 250)
	#button for speech recognition 
	addPlayers = QPushButton("Add Players", startScreen)
	addPlayers.clicked.connect(exit) #will go into speech recognition mode
	addPlayers.move(375, 300)
	startScreen.show()
	app.exec_()
#chooseLocation()
#chooseSceneSettings()
main()


#if _name_ == '_main_':
#	main()
