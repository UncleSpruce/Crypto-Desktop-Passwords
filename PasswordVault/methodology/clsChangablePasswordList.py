'''
Created on Jul 23, 2015
@author: Daniel Bruce
'''
from methodology.clsPasswordList import PasswordList
from methodology.clsGenericRecovery import GenericRecovery

class ChangablePasswordList(PasswordList):
	'''
	classdocs
	'''
	def __init__(self, pList = None):
		'''
		Constructor
		'''
		if pList is None:
			pList = []
		self.list = pList	
		super(ChangablePasswordList, self).__init__(pList)
		
	def append(self, pItem):
		# Replace an existing key that has the item.
		super(ChangablePasswordList, self).popByIdentifier(pItem.identifier())
		# Do this is the vault has no matching mapping signature.
		super(ChangablePasswordList, self).append(pItem)
		return		