'''
Created on Jul 22, 2015
@author: Daniel Bruce
'''
from functionality.clsPivotedVault import PivotedVault
from methodology.clsPasswordList import PasswordList
from functionality.clsProgramPasswordData import ProgramPasswordData
import pickle

class ProgramState(object):
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
		self.vaultFileName = ""
		self.passwordData = ProgramPasswordData()
	
	def isOpen(self):
		if -1 in self.list.identifier():
			return True
		return False
	
	def openVault(self):
		#returns -1 if vault can't be opened. 0 otherwise.
		# An opened vault
		if self.isOpen():
			print("Warning: You tried to open an open vault.")
	
	def addPassword(self, pPasswordTuple):
		self.passwordData.addOutput(pPasswordTuple)
	
	def removePassword(self, pPasswordTuple):
		self.passwordData.removeOutput(pPasswordTuple)
		# Remove keys associated with password pair?
	
	def changePassword(self, pPasswordTuple):
		return
	
	def addInput(self, pInputList):
		self.passwordData.addInputList(pInputList)
		
	def addInputPlusPasswords(self, pInputList):
		self.addInput(pInputList)
		for i in pInputList.getList():
			self.addPassword(i)
		
	def removeInput(self, pInputList):
		self.passwordData.removeInputList(pInputList)
	

		
	def toString(self):
		print("Vault file name: ", self.vaultFileName)
		print("Vault contents:")
		print(self.vault.toString())
		print("The recovered password list:")
		print(self.recoveredList())