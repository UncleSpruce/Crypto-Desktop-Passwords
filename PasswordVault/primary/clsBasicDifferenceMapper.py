'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

class BasicDifferenceMapper(object):
	'''
	classdocs
	'''

	def __init__(self, pSource, pTarget):
		'''
		Constructor
		'''
		self.difference = pTarget - pSource
		
	def compute(self, pSource):
		return pSource + self.difference