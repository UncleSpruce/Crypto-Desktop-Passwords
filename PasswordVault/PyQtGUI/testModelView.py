'''
Created on Jul 26, 2015

@author: Daniel Bruce
'''

# from PyQt5 import QtCore, QtGui, QtWidgets
# import QSta
# import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QListView
# import PyQt5

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from random import randint

# Create a Qt application
app = QApplication(sys.argv)

# Our main window will be a QListView
vlist = QListView()
vlist.setWindowTitle('Honey-Do List')
vlist.setMinimumSize(600, 400)

# Create an empty model for the list's data
model = QStandardItemModel(vlist)

# Add some textual items
foods = [
	'Cookie dough', # Must be store-bought
	'Hummus', # Must be homemade
	'Spaghetti', # Must be saucy
	'Dal makhani', # Must be spicy
	'Chocolate whipped cream' # Must be plentiful
]

for food in foods:
	# Create an item with a caption
	item = QStandardItem(food)

	# Add a checkbox to it
	item.setCheckable(True)

	# Add the item to the model
	model.appendRow(item)

def on_item_changed(item):
	# If the changed item is not checked, don't bother checking others
	if not item.checkState():
		return

	# Loop through the items until you get None, which
	# means you've passed the end of the list
	i = 0
	while model.item(i):
		if not model.item(i).checkState():
			return
		i += 1
	
	app.quit()

model.itemChanged.connect(on_item_changed)

# Apply the model to the list view
vlist.setModel(model)

# Show the window and run the app
vlist.show()
app.exec_()