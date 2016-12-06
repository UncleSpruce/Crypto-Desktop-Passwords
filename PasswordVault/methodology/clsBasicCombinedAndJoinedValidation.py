'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''

class BasicCombinedAndJoinedValidation(object):
	'''
	classdocs
	'''
	def __init__(self, pModulus = None, pBase = None):
		'''
		Constructor
		'''
		if pBase is None:
			pBase = 2
		if pModulus is None:
			pModulus = 7
			#Throw exception?
		self.modulus = pModulus
		self.base = pBase
		
	def defineMap(self, pModulus, pBase):
		self.modulus = pModulus
		self.base = pBase
	
	def compute(self, pArgument):
		return pow(self.base, pArgument, self.modulus) 