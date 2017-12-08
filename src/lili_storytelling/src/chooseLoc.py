import sys
import ExtendedQLabel
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

app = QApplication(sys.argv)
w = QWidget()
w.resize(900,600)

title = QLabel('Select a Location for Scene 1', w)
title.setStyleSheet("font: bold 15pt")
title.move(320,30)

loc1 = QLabel(w)
loc1.setGeometry(100,100,200,150)
loc1.setPixmap(QPixmap('city.jpg'))
loc1Text = QLabel("City",w)
loc1Text.setGeometry(180,235,100,100)


loc2 = QLabel(w)
loc2.setGeometry(350,100,200,150)
loc2.setPixmap(QPixmap('mountains.jpg'))
loc2Text = QLabel("Mountains",w)
loc2Text.setGeometry(420,235,100,100)


loc3 = QLabel(w)
loc3.setGeometry(600,100,200,150)
loc3.setPixmap(QPixmap('forest.jpg'))
loc3Text = QLabel("Forest",w)
loc3Text.setGeometry(670,235,100,100)


loc4 = QLabel(w)
loc4.setGeometry(100,320,200,150)
loc4.setPixmap(QPixmap('ocean.jpg'))
loc4Text = QLabel("Ocean",w)
loc4Text.setGeometry(170,455,100,100)


loc5 = QLabel(w)
loc5.setGeometry(350,320,200,150)
loc5.setPixmap(QPixmap('farm.jpg'))
loc5Text = QLabel("Farm",w)
loc5Text.setGeometry(430,455,100,100)

#class ExtendedQLabel(QLabel):
#	def __init(self, parent):
#		QLabel.__init(self, parent)
#	def mouseReleaseEvent(self, ev):
#		self.emit(SIGNAL('clicked()'))
def on_loc_click(self):
	print('loc clicked')

	#self.setStyleSheet("border: 1px solid black");


loc6 = QLabel(w)
loc6.setGeometry(600,320,200,150)
loc6.setPixmap(QPixmap('desert.jpg'))
loc6Text = QLabel("Desert",w)
loc6Text.setGeometry(670,455,100,100)

#loc6.connect(SIGNAL('clicked()'), on_loc_click)

#loc6.mousePressEvent = on_loc_click
#loc6.setSyleSheet("border: 1px solid black")

choose = QPushButton("Choose this location", w)
choose.clicked.connect(exit)
choose.move(375,550)

#view.show()
w.show()
app.exec_()
app.deleteLater()
