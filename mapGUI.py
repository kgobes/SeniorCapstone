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
#global numscene
numscene = 8

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
	
	loc1 = QLabel(chooseLocScreen)
	loc1.setGeometry(100,100,200,150)
	loc1.setPixmap(QPixmap('locimages/city.jpg'))
	loc1Text = QLabel("City",chooseLocScreen)
	loc1Text.setGeometry(180,235,100,100)


	loc2 = QLabel(chooseLocScreen)
	loc2.setGeometry(350,100,200,150)
	loc2.setPixmap(QPixmap('locimages/mountains.jpg'))
	loc2Text = QLabel("Mountains",chooseLocScreen)
	loc2Text.setGeometry(420,235,100,100)


	loc3 = QLabel(chooseLocScreen)
	loc3.setGeometry(600,100,200,150)
	loc3.setPixmap(QPixmap('locimages/forest.jpg'))
	loc3Text = QLabel("Forest",chooseLocScreen)
	loc3Text.setGeometry(670,235,100,100)


	loc4 = QLabel(chooseLocScreen)
	loc4.setGeometry(100,320,200,150)
	loc4.setPixmap(QPixmap('locimages/ocean.jpg'))
	loc4Text = QLabel("Ocean",chooseLocScreen)
	loc4Text.setGeometry(170,455,100,100)


	loc5 = QLabel(chooseLocScreen)
	loc5.setGeometry(350,320,200,150)
	loc5.setPixmap(QPixmap('locimages/farm.jpg'))
	loc5Text = QLabel("Farm",chooseLocScreen)
	loc5Text.setGeometry(430,455,100,100)

	loc6 = QLabel(chooseLocScreen)
	loc6.setGeometry(600,320,200,150)
	loc6.setPixmap(QPixmap('locimages/desert.jpg'))
	loc6Text = QLabel("Desert",chooseLocScreen)
	loc6Text.setGeometry(670,455,100,100)

	#loc6.connect(SIGNAL('clicked()'), on_loc_click)
	#loc6.mousePressEvent = on_loc_click
	#loc6.setSyleSheet("border: 1px solid black")

	choose = QPushButton("Choose this location", chooseLocScreen)
	#figure out how to read in selection 
	#	numscene = 6
	
	choose.clicked.connect(chooseActivities)
	choose.move(375,550)

	global numscenes	
	print(numscenes.currentText())
	global numscene
	numscene = int(str(numscenes.currentText()))

	chooseLocScreen.show()

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
#button.clicked.connect(chooseLocation(numscenes.itemData(numscene.currentIndex())))
#	print(chooseLocation(numscenes.currentText()))
	button.move(350, 400)
	
	#declaration of map object for this instance
	#myMap = 

	sceneSettingsScreen.show()
	#app.exec_()


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
