'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from primary.clsBasicDifferenceMapper import BasicDifferenceMapper
from primary.clsBasicStringIntConverter import BasicStringIntConverter
from primary.clsBasicHash import BasicHash

class BasicMapIntermediateToResult(object):
	'''
	classdocs
	'''
	def __init__(self, pOneWayHashFunction = BasicHash(), pConverter = BasicStringIntConverter(), pDifferenceMapper = BasicDifferenceMapper()):
		'''
		Constructor
		'''
		self.oneWayHashFunction = pOneWayHashFunction
		self.differenceMapper = pDifferenceMapper
		self.converter = pConverter
	
	def defineMap(self, pIntermediate, pResult):
		#lclHashed = self.oneWayHashFunction.compute(pIntermediate)
		lclHashed = self.oneWayHashFunction.compute(pIntermediate)
		lclResultAsInt = self.converter.toInt(pResult)
		return self.differenceMapper.defineMap(lclHashed, lclResultAsInt)
	
	def compute(self, pIntermediate):
		lclHashed = self.oneWayHashFunction.compute(pIntermediate)
		lclResultAsInt = self.differenceMapper.compute(lclHashed)
		return self.converter.toString(lclResultAsInt)
	
	def encode(self):
		return self.differenceMapper.difference