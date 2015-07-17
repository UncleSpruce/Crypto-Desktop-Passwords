'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

class BasicStringJoinerAndCombiner(object):
	'''
	classdocs
	'''
	def __init__(self, pStringJoiner, pCombiner):
		'''
		Constructor
		'''
		self.stringJoiner = pStringJoiner
		self.combiner = pCombiner
		
	def joinAndCombine(self, pPasswordList):
		lclList = []
		for i in pPasswordList.list:
			lclList.append(self.stringJoiner.joinTwoStrings(i.identifier(), i.password()))
		return self.combiner.combine(lclList)