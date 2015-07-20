'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicLabelledKey import BasicLabelledKey
from methodology.clsBasicRecovery import BasicRecovery

class Vault(object):
	'''
	classdocs
	'''
	def __init__(self, pList = [], pRecoveryMethod = BasicRecovery()):
		'''
		Constructor
		'''
		self.recoveryMethod = pRecoveryMethod
		self.list = []
		
	def append(self, pItem):
		if not isinstance(pItem, BasicLabelledKey):
			raise TypeError("Argument passed into append function is not a BasicLabelledKey.")
		self.list.append(pItem)
		
	def getList(self):
		return self.list
	
	def popByName(self, pKeyName):
		for i in self.list:
			if i.name() == pKeyName:
				return self.list.pop(i)
	
	def pop(self):
		return self.list.pop()
			
	def recover(self, pInputPasswordList):
		return self.recoveryMethod.recover(self, pInputPasswordList)
	
	def toString(self):
		returnString = ""
		for i in self.list:
			returnString += i.toString() + "\n"
		return returnString