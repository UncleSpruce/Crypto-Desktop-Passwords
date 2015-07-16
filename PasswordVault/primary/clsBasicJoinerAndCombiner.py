'''
Created on Jul 15, 2015

@author: Owner
'''

class BasicJoinerAndCombiner(object):
	'''
	classdocs
	'''
	def __init__(self, pJoiner, pCombiner):
		'''
		Constructor
		'''
		self.joiner = pJoiner
		self.combiner = pCombiner
		
	def joinAndCombine(self, pPasswordList):
		
		