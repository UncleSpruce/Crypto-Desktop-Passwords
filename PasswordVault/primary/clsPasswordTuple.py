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
		
	def identifier(self):
		return self.tuple[0]
	
	def password(self):
		return self.tuple[1]