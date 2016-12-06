'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

from methodology.clsBasicKeyGenerator import BasicKeyGenerator
from methodology.clsBasicLabelledKey import BasicLabelledKey
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator

#Obselete class

class BasicLabelledKeyGenerator(object):
	'''
	classdocs
	'''
	def __init__(self, pKeyGen = BasicKeyGenerator()):
		'''
		Constructor
		'''
		self.keyGen = pKeyGen
	
	def generate(self, pPasswordList, pResult, pName = BasicBigIntGenerator(64).generate()):
		lclKey = self.keyGen.generateKey(pPasswordList, pResult.password())
		return BasicLabelledKey(pName,pPasswordList.getIdentifierList(), pResult.identifier(), "Basic", lclKey)
		
