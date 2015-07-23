'''
Created on Jul 23, 2015

@author: Daniel Bruce
'''
from methodology.clsSimpleVault import SimpleVault
from methodology.clsPasswordList import PasswordList

class ProgramPasswordData(object):
	'''
	classdocs
	'''
	def __init__(self, pVault = None, pPasswordList = None):
		'''
		Constructor
		'''
		if pVault is None:
			pVault = SimpleVault()
		if pPasswordList is None:
			pPasswordList = PasswordList()
		self.vault = pVault
		self.passwordList = pPasswordList
	
	def getPasswordList(self):
		return self.passwordList
	
	def getVault(self):
		return self.vault
	
	def addPassword(self, pPasswordTuple):
		self.vault.addPassword(pPasswordTuple)
		self.passwordList.append(pPasswordTuple)
	
	def removePassword(self, pPasswordTuple):
		self.vault.removePassword(pPasswordTuple)
		self.passwordList.remove(pPasswordTuple)
	
	def addInput(self, pInputList):
		self.vault.addInput(pInputList)
		
	def removeInput(self, pInputList):
		self.vault.removeInput(pInputList)
		
	def toString(self):
		returnString = ""
		returnString = self.vault.toString()
		returnString = "\n"
		returnString = self.passwordList.toString()
		return returnString
	
	def createPickledVault(self):
		return self.vault.createPickledVault()