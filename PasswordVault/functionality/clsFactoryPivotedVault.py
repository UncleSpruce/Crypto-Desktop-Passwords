'''
Created on Jul 22, 2015
@author: Daniel Bruce
'''

from functionality.clsPivotedVault import PivotedVault

class FactoryPivotedVault(object):
	'''
	classdocs
	'''
	def __init__(self, params):
		'''
		Constructor
		'''	
		
	def newPivotedVault(self):
		return PivotedVault()
	
	def recoverPivotedVault(self, pSimpleVault, pPasswordList):
		# If -1 is not in the recovered list of identifiers then return -1. Otherwise return the vault.
		# Pivoted vault constructor: def __init__(self, pVault = SimpleVault([]), pIntermediate = BasicBigIntGenerator().generate(), pGenerator = SimpleLabelledKeyGenerator()):
		lclIntermediate = -1
		lclRecoveredList = pSimpleVault.recover(pPasswordList)
		for i in lclRecoveredList.getIdentifierList():
			if i.identifier() == -1:
				lclIntermediate = i.password()
				return PivotedVault(pSimpleVault, lclIntermediate)
		return -1	