'''
Created on Jul 23, 2015

@author: Daniel Bruce
'''
from methodology.clsSimpleVault import SimpleVault
from methodology.clsPasswordList import PasswordList
from functionality.clsOpenableVault import OpenableVault
from methodology.clsChangablePasswordList import ChangablePasswordList

class ProgramPasswordData(object):
	'''
	classdocs
	'''
	def __init__(self, pVault = None, pPasswordList = None):
		'''
		Constructor
		'''
		if pVault is None:
			pVault = OpenableVault()
		if pPasswordList is None:
			pPasswordList = {}
		self.vault = pVault
		self.passwordList = pPasswordList
	
	def getVaultForSaving(self):
		return self.vault.getVaultForSaving()
	
	def getPasswordList(self):
		return self.passwordList
	
	def getVault(self):
		return self.vault
	
	def addPassword(self, pPasswordTuple):
		self.vault.addPassword(pPasswordTuple)
		print ("Adding Tuple (", pPasswordTuple[0], ",", pPasswordTuple[1], ")")
		self.passwordList[pPasswordTuple[0]] = pPasswordTuple[1]
		self.vault.open(self.passwordList)
	
	def removePassword(self, pPasswordTuple):
		self.vault.removePassword(pPasswordTuple)
		self.passwordList.remove(pPasswordTuple)
	
	def addInput(self, pInputList):
		self.vault.addInput(pInputList)
		
	def addInputWithPasswords(self, pInputList):
		self.addInput(pInputList)
		for i in pInputList:
			self.addPassword((i, pInputList[i]))
		return		
	
	def removeInput(self, pInputList):
		self.vault.removeInput(pInputList)
		
	def toString(self):
		returnString = ""
		returnString += "Vault:\n" + self.vault.toString()
		returnString += ""
		returnString += "Password List: "
		returnString += str(self.passwordList) + "\n"
		return returnString
	
	def createPickledVault(self):
		return self.vault.createPickledVault()