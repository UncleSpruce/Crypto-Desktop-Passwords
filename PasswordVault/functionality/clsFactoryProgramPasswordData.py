'''
Created on Jul 23, 2015

@author: Daniel Bruce
'''
from functionality.clsOpenableVault import OpenableVault
from functionality.clsProgramPasswordData import ProgramPasswordData

class FactoryProgramPasswordData(object):
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
	
	def build(self, pVault = None, pPasswordList = None):
		return ProgramPasswordData(pVault, pPasswordList)