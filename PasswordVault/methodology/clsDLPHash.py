'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''

import hashlib
from methodology.iHashMethodology import iHashMethodology
from methodology.clsBasicStringIntConverter import BasicStringIntConverter
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator

class DLPHash(iHashMethodology):
	'''
	classdocs
	'''
	def __init__(self, pModulus = None, pBase = None):
		'''
		Constructor
		'''
		if pModulus is None:
			pModulus = BasicBigIntGenerator().generate()
		if pBase is None:
			pBase = 2
		self.defineMap(pModulus, pBase)
		
	def defineMap(self, pModulus, pBase):
		self.modulus = pModulus
		self.base = pBase
	
	def compute(self, pArgument):
		return pow(self.base, pArgument, self.modulus)
	
	def toString(self):
		return "(" + str(self.modulus) + "," + str(self.base) + ")"