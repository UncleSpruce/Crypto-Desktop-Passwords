'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

from methodology.clsBasicKeyGenerator import BasicKeyGenerator
from methodology.clsBasicLabelledKey import BasicLabelledKey

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
		
