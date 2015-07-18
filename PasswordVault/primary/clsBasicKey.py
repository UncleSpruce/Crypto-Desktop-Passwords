'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from primary.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult
from primary.clsBasicMapInputToIntermediate import BasicMapInputToIntermediate

class BasicKey(object):
	'''
	classdocs
	'''	
	
	def __init__(self, pInputToIntermediate = BasicMapInputToIntermediate(), pIntermediateToResult = BasicMapIntermediateToResult()):
		'''
		Constructor
		'''
		self.inputToIntermediate = pInputToIntermediate
		self.intermediateToResult = pIntermediateToResult
		
	def compute(self, pPasswordList):
		lclIntermediate = self.inputToIntermediate.compute(pPasswordList)
		lclResult = self.intermediateToResult.compute(lclIntermediate)
		return lclResult
	
	def encode(self):
		return (self.inputToIntermediate.encode(), self.intermediateToResult.encode())