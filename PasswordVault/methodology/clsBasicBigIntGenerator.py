'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from methodology.iBigIntGenerator import iBigIntGenerator
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
		return random.getrandbits(self.numBits)