'''
Created on Jul 21, 2015

@author: Daniel Bruce

'''
from methodology.clsSimpleVault import SimpleVault
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator

class IntermediateVault(object):
	'''
	classdocs
	'''
	def __init__(self, pVault = SimpleVault([]), pPasswordList = []):
		'''
		Constructor
		'''
		
		#the identifier for the intermediate is -1
		
		self.vault = pVault
		self.passwordList = pPasswordList
		self.passwordList.append(PasswordTuple(-1, pIntermediate))
	
	def getVault(self):
		return self.vault

	def getPasswordList(self):
		return self.passwordList
	
	def addPassword(self, pPasswordTuple):
		# Returns -1 if the password can't be added.
		if not isinstance(pPasswordTuple, PasswordTuple):
			raise TypeError("Argument passed into append function for PasswordList is not a PasswordTuple.")
		for i in self.passwordList.getIdentifierList():
			if str(pPasswordTuple.identifer()) == str(i):
				return -1
		self.passwordList.append(pPasswordTuple)
		return 0
	
	def addKey(self, pKey):
		for i in self.vault.getList():
			if str(i) == str(pKey):
				return -1 
		self.vault.append(pKey)
		return 0
	
	def popKey(self, pKey):
		return self.vault.pop(pKey)
	
	def popKeyByName(self, pKeyName):
		return self.vault.popByName(pKeyName)
	
	def recover(self):
		self.passwordList = self.vault.recover(self.passwordList)
		
	def toString(self):
		returnString = ""
		print("Vault contents:")
		print(self.vault.toString())
		print("Password list contents:")
		print(self.passwordList.toString())
		return returnString