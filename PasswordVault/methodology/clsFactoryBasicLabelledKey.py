'''
Created on Jul 18, 2015

@author: Daniel Bruce
'''

#Obselete class

class FactoryBasicLabelledKey(object):
	'''
	classdocs
	'''
	def __init__(self, params):
		'''
		Constructor
		'''
	
	def __str__(self):
		return str(self.__dict__)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__
	
	def generateKeyFromEncoding(self, pString):
		# If a key cannot be generated then -1 is returned.
		