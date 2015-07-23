'''
Created on Jul 22, 2015

@author: Daniel Bruce
'''
from functionality.clsPivotedVault import PivotedVault
from methodology.clsPasswordList import PasswordList
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
		self.vault = PivotedVault()
		self.list = PasswordList()
	
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
		self.vault.addOutput(pPasswordTuple)
	
	def removePassword(self, pPasswordTuple):
		self.vault.removeOutput(pPasswordTuple)
	
	def addInput(self, pInputList):
		self.vault.addInputList(pInputList)
		
	def removeInput(self, pInputList):
		self.vault.removeInputList(pInputList)
	
	def openPickledVault(self, pFileName):
		with open (pFileName, "r") as myfile:
			lclVault = myfile.readlines()
		self.vault = pickle.loads(lclVault)
	
	def savePickledVault(self, pFileName):
		text_file = open(pFileName, "wb")
		text_file.write(self.vault.createPickledVault())
		text_file.close()
		
	def toString(self):
		print("Vault file name: ", self.vaultFileName)
		print("Vault contents:")
		print(self.vault.toString())
		print("The recovered password list:")
		print(self.recoveredList())