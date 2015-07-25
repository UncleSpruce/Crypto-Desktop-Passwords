'''
Created on Jul 23, 2015

@author: Daniel Bruce
'''
from methodology.clsSimpleVault import SimpleVault
from methodology.clsGenericRecovery import GenericRecovery

class SwappingVault(SimpleVault):
	'''
	classdocs
	'''
	def __init__(self, pList = None, pRecoveryMethod = GenericRecovery()):
		'''
		Constructor
		'''
		if pList is None:
			pList = []
		self.recoveryMethod = pRecoveryMethod
		self.list = pList	
		super(SwappingVault, self).__init__(pList, pRecoveryMethod)
		
	def append(self, pItem):
		# Replace an existing key that has the item.
		super(SwappingVault, self).removeByInputListIdentifiersAndResultIdentifier(pItem.identifierList(), pItem.resultIdentifier())
		# Do this is the vault has no matching mapping signature.
		super(SwappingVault, self).append(pItem)
		return