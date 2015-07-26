'''
Created on Jul 21, 2015

@author: Daniel Bruce
'''
from functionality.clsIntermediateVault import IntermediateVault
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from methodology.clsSimpleVault import SimpleVault
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator

class ControlledIntermediateVault(IntermediateVault):
	'''
	classdocs
	'''

	def __init__(self, pIntermediate = BasicBigIntGenerator().generate(), pVault = SimpleVault(), pPasswordList = {}, pGenerator = SimpleKeyGenerator()):
		'''
		Constructor
		'''
		self.intermediate = pIntermediate
		IntermediateVault.__init__(self, BasicBigIntGenerator().generate(), pVault, pPasswordList)
		
	def addInputList(self, pInputList):
		#super(ControlledIntermediateVault, self).methodName(arguments)
		#super(ControlledIntermediateVault, self)
		lclKey = self.gen.generate(pInputList, self.intermediate)
		return self.vault.append(lclKey)
		
	def addOutput(self, pPasswordTuple):
		lclKey = self.gen.generate(self.intermediate, pPasswordTuple)
		return self.vault.append(lclKey)