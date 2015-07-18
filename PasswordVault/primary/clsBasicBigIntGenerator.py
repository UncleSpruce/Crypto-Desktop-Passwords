'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from primary.iBigIntGenerator import iBigIntGenerator
import random

class BasicBigIntGenerator(iBigIntGenerator):
	'''
	classdocs
	'''
	
	def __init__(self, pNumBits = 512):
		'''
		Constructor
		'''
		self.numBits = pNumBits
	
	def generate(self):
		return 0#random.getrandbits(self.numBits)	