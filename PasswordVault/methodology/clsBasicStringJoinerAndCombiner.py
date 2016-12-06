'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicCombiner import BasicCombiner
from methodology.clsBasicStringJoiner import BasicStringJoiner

class BasicStringJoinerAndCombiner(object):
	'''
	classdocs
	'''
	def __init__(self, pStringJoiner = BasicStringJoiner(), pCombiner = BasicCombiner()):
		'''
		Constructor
		'''
		self.stringJoiner = pStringJoiner
		self.combiner = pCombiner
		
	def joinAndCombine(self, pPasswordList):
		lclList = []
		for i in pPasswordList:
			lclList.append(self.stringJoiner.joinTwoStrings(i, pPasswordList[i]))
		lclCombined = self.combiner.combine(lclList) 
		return lclCombined