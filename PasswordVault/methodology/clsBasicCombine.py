'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from methodology.iCombiningMethodology import iCombiningMethodology

class BasicCombine(iCombiningMethodology):
	'''
	classdocs
	'''
	def __init__(self, params):
		'''
		Constructor
		'''
		
	def combine(self, pList):
		total = 0
		for i in pList:
			total += i
		return total