'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
from methodology.clsSimpleKey import SimpleKey
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator
from methodology.clsSimpleLabelledKey import SimpleLabelledKey
from methodology.clsGenericLabelledKey import GenericLabelledKey
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator

class SimpleLabelledKeyGenerator(object):
	'''
	classdocs
	'''

	def __init__(self, pKeyGen = None):
		'''
		Constructor
		'''
		if pKeyGen is None:
			pKeyGen = SimpleKeyGenerator()
		self.keyGen = pKeyGen
	
	def generate(self, pPasswordList, pResult, pName = None):
		if pName == None:
			pName = str(BasicBigIntGenerator(64).generate())
		lclKey = self.keyGen.generate(pPasswordList, pResult[1])
		return GenericLabelledKey(pName, list(pPasswordList.keys()), pResult[0], lclKey)