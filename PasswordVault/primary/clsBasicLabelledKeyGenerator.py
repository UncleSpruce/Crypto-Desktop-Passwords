'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

from primary.clsBasicKeyGenerator import BasicKeyGenerator
from primary.clsBasicLabelledKey import BasicLabelledKey

class BasicLabelledKeyGenerator(object):
	'''
	classdocs
	'''
	def __init__(self, pKeyGen = BasicKeyGenerator()):
		'''
		Constructor
		'''
		self.keyGen = pKeyGen
	
	def generate(self, pPasswordList, pResult):
		lclKey = self.keyGen.generateKey(pPasswordList, pResult.password())
		return BasicLabelledKey(pPasswordList.getIdentifierList(), pResult.identifier(), "Basic", lclKey)
		
