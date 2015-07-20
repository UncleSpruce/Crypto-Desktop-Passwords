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
	def __init__(self, pModulus = BasicBigIntGenerator().generate(), pBase = 2):
		'''
		Constructor
		'''
		self.modulus = 7
		self.base = 2
		
	def defineMap(self, pModulus, pBase = 2):
		self.modulus = pModulus
		self.base = pBase
	
	def compute(self, pArgument):
		return pow(self.base, pArgument, self.modulus)