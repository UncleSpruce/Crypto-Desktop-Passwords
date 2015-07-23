'''
Created on Jul 23, 2015

@author: Daniel Bruce
'''
from methodology.clsSimpleVault import SimpleVault
from methodology.clsPasswordList import PasswordList
from methodology.clsPasswordTuple import PasswordTuple
from functionality.clsPivotedVault import PivotedVault

class OpenableVault(object):
	'''
	classdocs
	'''
	def __init__(self, pVault = None):
		'''
		Constructor
		'''
		if pVault is None:
			pVault = SimpleVault()
# 		if pPasswordList is None:
# 			pPasswordList = PasswordList()
		self.vault = pVault
	
	def isOpen(self):
		if isinstance(self.vault, PivotedVault):
			return True
		return False
	
	def open(self, pPasswordList):
		if self.isOpen():
			print("Warning: Open attempted on an open vault.")
		pRecoveredList = self.vault.recover(pPasswordList)
		lclPivot = pRecoveredList.getByIdentifier(-1)
		if lclPivot == -1:
			return -1
		lclPivotPassword = lclPivot.password()
		self.vault = PivotedVault(self.vault, lclPivotPassword)
		return 0
	
	def getVault(self):
		return self.vault
		
	def addPassword(self, pPasswordTuple):
		if not isinstance(pPasswordTuple, PasswordTuple):
			raise TypeError("Argument passed into append function for PasswordList is not a PasswordTuple.")
		if not self.isOpen():
			return -1
		self.vault.addOutput(pPasswordTuple)

	def removePassword(self, pPasswordTuple):
		if not isinstance(pPasswordTuple, PasswordTuple):
			raise TypeError("Argument passed into append function for PasswordList is not a PasswordTuple.")
		if not self.isOpen():
			return -1
		self.vault.removeOutput(pPasswordTuple)
	
	def addInput(self, pInputList):
		if not isinstance(pInputList, PasswordList):
			raise TypeError("Argument passed into append function for PasswordList is not a PasswordList.")
		if not self.isOpen():
			return -1
		self.vault.addInputList(pInputList)
		return 0
	
	def removeInput(self, pInputList):
		if not isinstance(pInputList, PasswordList):
			raise TypeError("Argument passed into append function for PasswordList is not a PasswordList.")		
		if not self.isOpen():
			return -1
		self.vault.removeInputList(pInputList)
		return 0
	
	def toString(self):
		return self.vault.toString()
	
	def createPickledVault(self):
		return self.vault.createPickledVault()