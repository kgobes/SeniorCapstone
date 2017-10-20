import sys
import ExtendedQLabel
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

#def main():
#	print('hey')
#	chooseLocation()
def chooseLocation():	
	title = QLabel('Select a Location for Scene 1', chooseLocScreen)
	title.setStyleSheet("font: bold 15pt")
	title.move(320,30)
	
	loc1 = QLabel(chooseLocScreen)
	loc1.setGeometry(100,100,200,150)
	loc1.setPixmap(QPixmap('city.jpg'))
	loc1Text = QLabel("City",chooseLocScreen)
	loc1Text.setGeometry(180,235,100,100)


	loc2 = QLabel(chooseLocScreen)
	loc2.setGeometry(350,100,200,150)
	loc2.setPixmap(QPixmap('mountains.jpg'))
	loc2Text = QLabel("Mountains",chooseLocScreen)
	loc2Text.setGeometry(420,235,100,100)


	loc3 = QLabel(chooseLocScreen)
	loc3.setGeometry(600,100,200,150)
	loc3.setPixmap(QPixmap('forest.jpg'))
	loc3Text = QLabel("Forest",chooseLocScreen)
	loc3Text.setGeometry(670,235,100,100)


	loc4 = QLabel(chooseLocScreen)
	loc4.setGeometry(100,320,200,150)
	loc4.setPixmap(QPixmap('ocean.jpg'))
	loc4Text = QLabel("Ocean",chooseLocScreen)
	loc4Text.setGeometry(170,455,100,100)


	loc5 = QLabel(chooseLocScreen)
	loc5.setGeometry(350,320,200,150)
	loc5.setPixmap(QPixmap('farm.jpg'))
	loc5Text = QLabel("Farm",chooseLocScreen)
	loc5Text.setGeometry(430,455,100,100)

	loc6 = QLabel(chooseLocScreen)
	loc6.setGeometry(600,320,200,150)
	loc6.setPixmap(QPixmap('desert.jpg'))
	loc6Text = QLabel("Desert",chooseLocScreen)
	loc6Text.setGeometry(670,455,100,100)

	#loc6.connect(SIGNAL('clicked()'), on_loc_click)
	#loc6.mousePressEvent = on_loc_click
	#loc6.setSyleSheet("border: 1px solid black")

	choose = QPushButton("Choose this location", chooseLocScreen)
	#choose.clicked.connect(chooseSceneSettings())
	QtCore.QObject.connect(choose, QtCore.SIGNAL('clicked()'), chooseSceneSettings())	
	choose.move(375,550)

	chooseLocScreen.show()
	app.exec_()
	app.deleteLater()
def chooseSceneSettings():
	chooseLocScreen.hide()
	button = QPushButton("Done", sceneSettingsScreen)
	button.clicked.connect(exit)
	button.move(375, 550)
	sceneSettingsScreen.show()
chooseLocation()
#if _name_ == '_main_':
#	main()
