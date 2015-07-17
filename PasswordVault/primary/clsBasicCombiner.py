'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from primary.iCombiningMethodology import iCombiningMethodology

class BasicCombiner(iCombiningMethodology):
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
		
	def combine(self, pList):
		total = 0
		for i in pList:
			total += i
		return total