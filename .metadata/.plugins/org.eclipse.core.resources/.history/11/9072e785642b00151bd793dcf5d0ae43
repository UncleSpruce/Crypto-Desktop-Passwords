'''
Created on Jul 15, 2015

@author: Owner
'''

class BasicMapIntermediateToResult(object):
	'''
	classdocs
	'''
	def __init__(self, pOneWayHashFunction, pIntermediate, pResult):
		'''
		Constructor
		'''
		self.oneWayHashFunction = pOneWayHashFunction
		lclHashed = pOneWayHashFunction.compute(pIntermediate)
		self.differenceMapper = BasicDifferenceMapper(lclHashed, pResult)
	
	def mapToResult(self, pIntermediate):
		return self.differenceMapper.compute(self.oneWayHashFunction.compute(pIntermediate))