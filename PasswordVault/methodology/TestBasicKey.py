'''
Created on Jul 17, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsBasicStringJoiner import BasicStringJoiner
from methodology.clsBasicCombiner import BasicCombiner
from methodology.clsBasicDifferenceMapper import BasicDifferenceMapper
from methodology.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from methodology.clsBasicMapInputToIntermediate import BasicMapInputToIntermediate
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsBasicHash import BasicHash
from methodology.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult
from methodology.clsBasicStringIntConverter import BasicStringIntConverter
from methodology.clsBasicKey import BasicKey
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from methodology.clsBasicKeyGenerator import BasicKeyGenerator

class BasicKeyTest(unittest.TestCase):

	def sampleCase(self, pPasswordList, pResult):
		#lclStringIntConverter = BasicStringIntConverter()
		#lclStringJoiner = BasicStringJoiner(lclStringIntConverter)
		#lclCombiner = BasicCombiner()
		#lclJoinerAndCombiner = BasicStringJoinerAndCombiner(lclStringJoiner, lclCombiner)
		#lclDifferenceMapper = BasicDifferenceMapper()
		#lclMapInputToIntermediate = BasicMapInputToIntermediate()
		#lclBasicKeyGenerator = BasicBigIntGenerator()
		#lclBasicMapIntermediateToResult = BasicMapIntermediateToResult()
		
		lclBasicKeyGenerator = BasicKeyGenerator()
		lclKey = lclBasicKeyGenerator.generateKey(pPasswordList, pResult)
		#print(lclKey.compute(pPasswordList))
		#print(pResult)
		self.assertEqual(lclKey.compute(pPasswordList), pResult)		

	def test_FullFunctionality(self):
		print("Running FullFunctionality for BasicKeyTest. ")
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclPasswordList = PasswordList([])
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)

		self.sampleCase(lclPasswordList, "")
		self.sampleCase(lclPasswordList, "Jeff Henry")
		self.sampleCase(lclPasswordList, "@@@@@@@@@@@@@@@@@")
		self.sampleCase(lclPasswordList, "%@%@%^#&")
		self.sampleCase(lclPasswordList, "hg hg hg hg")

	def test_createSampleKey(self):
		print("Running createSampleKey for BasicKeyTest.")
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclPasswordList = PasswordList([])
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)
		
		lclBasicKeyGenerator = BasicKeyGenerator()
		lclKey = lclBasicKeyGenerator.generateKey(lclPasswordList, "Grazzly")
		print(lclKey.encode())
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()