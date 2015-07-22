'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

class PasswordTuple(object):
	'''
	classdocs
	'''
	def __init__(self, pIdentifier, pPassword):
		'''
		Constructor
		'''
		self.tuple = (pIdentifier, pPassword)
	
	def __str__(self):
		return str(self.__dict__)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__

	def __key(self):
		return self.tuple

	def __hash__(self):
		return hash(self.__key())
		
	def identifier(self):
		return self.tuple[0]
	
	def password(self):
		return self.tuple[1]
	
	def toString(self):
		return "(" + str(self.tuple[0]) + "," + str(self.tuple[1]) + ")"
	
	def getTuple(self):
		return (self.tuple[0], self.tuple[1])