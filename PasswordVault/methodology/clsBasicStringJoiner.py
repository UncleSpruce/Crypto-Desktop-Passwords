'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from methodology.iJoiningBehavior import iJoiningBehavior
from methodology.clsBasicStringIntConverter import BasicStringIntConverter

class BasicStringJoiner(iJoiningBehavior):
	'''
	classdocs
	'''

	def __init__(self, pConverter = BasicStringIntConverter()):
		'''
		Constructor
		'''
		self.converter = pConverter
	
	def joinTwoStrings(self, pString1, pString2):
		return self.converter.toInt(pString1) * self.converter.toInt(pString2)	