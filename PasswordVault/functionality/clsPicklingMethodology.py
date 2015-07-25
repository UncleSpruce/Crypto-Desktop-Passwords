'''
Created on Jul 23, 2015
@author: Daniel Bruce
'''
import pickle
import json

class PicklingMethodology(object):
	'''
	classdocs
	'''

	def __init__(self):
		'''
		Constructor
		'''
	def SaveVaultAsJson(self, pPasswordData, pFilename):
		encoded = json.dumps(obj)
		
	def GetVaultFromJson(self, pFilename):
		pass
	
	def saveVault(self, pPasswordData, pFilename):
		lclVault = pPasswordData.getVaultForSaving()
		with open(pFilename, 'wb') as f:
			pickle.dump(lclVault, f)

	def getVaultFromFile(self, pFileName):
		with open(pFileName, 'rb') as f:
			mynewlist = pickle.load(f)
		return mynewlist