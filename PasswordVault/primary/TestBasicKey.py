'''
Created on Jul 17, 2015

@author: Daniel Bruce
'''
import unittest
from primary.clsBasicStringJoiner import BasicStringJoiner
from primary.clsBasicCombiner import BasicCombiner
from primary.clsBasicDifferenceMapper import BasicDifferenceMapper
from primary.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from primary.clsBasicMapInputToIntermediate import BasicMapInputToIntermediate
from primary.clsPasswordTuple import PasswordTuple
from primary.clsPasswordList import PasswordList
from primary.clsBasicHash import BasicHash
from primary.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult
from primary.clsBasicStringIntConverter import BasicStringIntConverter
from primary.clsBasicKey import BasicKey
from primary.clsBasicBigIntGenerator import BasicBigIntGenerator
from primary.clsBasicKeyGenerator import BasicKeyGenerator

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
		print(lclKey.compute(pPasswordList))
		print(pResult)
		self.assertEqual(lclKey.compute(pPasswordList), pResult)		

	def test_FullFunctionality(self):
		print("Running FullFunctionality for BasicKeyTest. ")
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclPasswordList = PasswordList()
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)

		self.sampleCase(lclPasswordList, "")
		self.sampleCase(lclPasswordList, "Jeff Henry")

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()