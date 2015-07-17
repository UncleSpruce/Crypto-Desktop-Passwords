'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

class BasicMapInputToIntermediate(object):
	'''
	classdocs
	'''
	def __init__(self, pDifferenceMapper, pStringJoinerAndCombiner):
		'''
		Constructor
		'''
		self.stringJoinerAndCombiner = pStringJoinerAndCombiner
		self.differenceMapper = pDifferenceMapper
	
	def defineMap(self, pPasswordList, pIntermediate):
		lclJoinedAndCombinedInput = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
		self.differenceMapper.defineMapper(lclJoinedAndCombinedInput, pIntermediate)
	
	def compute(self, pPasswordList):
		lclJandC = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
		return self.differenceMapper.compute(lclJandC)