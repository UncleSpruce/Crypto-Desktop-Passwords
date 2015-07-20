'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''

class BasicCombinedAndJoinedValidation(object):
	'''
	classdocs
	'''
	def __init__(self, pModulus = 7, pBase = 2):
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