'''
Created on Jul 22, 2015
@author: Daniel Bruce
'''
from functionality.clsPivotedVault import PivotedVault
from methodology.clsPasswordList import PasswordList
from functionality.clsProgramPasswordData import ProgramPasswordData
import pickle
from functionality.clsPicklingMethodology import PicklingMethodology

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
		self.pickler = PicklingMethodology()
# 	def isOpen(self):
# 		if -1 in self.list.identifier():
# 			return True
# 		return False
	
	def addPassword(self, pPasswordTuple):
		self.passwordData.addPassword(pPasswordTuple)
	
	def removePassword(self, pPasswordTuple):
		self.passwordData.removePassword(pPasswordTuple)
		# Remove keys associated with password pair?
			
	def addInputPlusPasswords(self, pInputList):
		self.passwordData.addInputWithPasswords(pInputList)
		#self.addInput(pInputList)
		#for i in pInputList.getList():
		#	self.addPassword(i)
	
	def addInput(self, pInputList):
		self.passwordData.addInput(pInputList)
	
	def setFileName(self, pFileName):
		self.vaultFileName = pFileName
	
	def saveVault(self):
		self.pickler.saveVault(self.passwordData, self.vaultFileName)
	
	def loadVault(self):
		#Check for malicious pickling
		return self.pickler.getVaultFromFile(self.vaultFileName)
	
	def removeInput(self, pInputList):
		self.passwordData.removeInput(pInputList)
	
	def displayedPasswords(self):
		lclPasswordList = self.passwordData.getPasswordList()
		del lclPasswordList["Intermediate Constant: 3161379751047332383565"]
		return lclPasswordList
		
	def toString(self):
		print("Password Data contents:")
		print(self.vault.toString())
		#print("The recovered password list:")
		#print(self.recoveredList())