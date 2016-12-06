'''
Created on Jul 17, 2015

@author: Daniel Bruce
'''

# Obselete class

class BasicSpreader(object):
	'''
	classdocs
	'''
	def __init__(self, pGenerator):
		'''
		Constructor
		'''
		self.generator = pGenerator
	
	def spread(self, pResultList):
		return pResultList