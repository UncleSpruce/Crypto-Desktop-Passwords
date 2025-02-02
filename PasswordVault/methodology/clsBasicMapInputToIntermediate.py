'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from methodology.clsBasicDifferenceMapper import BasicDifferenceMapper

# Obselete Class

class BasicMapInputToIntermediate(object):
	'''
	classdocs
	'''
	def __init__(self, pDifferenceMapper = BasicDifferenceMapper(), pStringJoinerAndCombiner = BasicStringJoinerAndCombiner()):
		'''
		Constructor
		'''
		self.stringJoinerAndCombiner = pStringJoinerAndCombiner
		self.differenceMapper = pDifferenceMapper
	
	def defineMap(self, pPasswordList, pIntermediate):
		lclJoinedAndCombinedInput = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
		return self.differenceMapper.defineMap(lclJoinedAndCombinedInput, pIntermediate)
	
	def compute(self, pPasswordList):
		lclJandC = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
		return self.differenceMapper.compute(lclJandC)
	
	def encode(self):
		return self.differenceMapper.encode()
	
	def toString(self):
		return self.differenceMapper.toString()