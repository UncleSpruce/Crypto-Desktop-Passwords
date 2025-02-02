'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

class BasicDifferenceMapper(object):
	'''
	classdocs
	'''

	def __init__(self, pDifference = None):
		'''
		Constructor
		'''
		if pDifference is None:
			pDifference = 0
		self.difference = pDifference
	
	def defineMap(self, pSource, pTarget):
		self.difference = pTarget - pSource
		return self.difference
		
	def compute(self, pSource):
		return pSource + self.difference
	
	def encode(self):
		return self.difference
	
	def toString(self):
		return str(self.difference)