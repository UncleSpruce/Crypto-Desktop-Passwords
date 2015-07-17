'''
Created on Jul 17, 2015

@author: Daniel Bruce
'''
import unittest
from primary.clsBasicStringIntConverter import BasicStringIntConverter
from primary.clsBasicStringJoiner import BasicStringJoiner
from primary.clsBasicCombiner import BasicCombiner
from primary.clsBasicDifferenceMapper import BasicDifferenceMapper
from primary.clsBasicStringJoinerAndCombiner import BasicStringJoinerAndCombiner
from primary.clsBasicMapInputToIntermediate import BasicMapInputToIntermediate
from primary.clsPasswordTuple import PasswordTuple
from primary.clsPasswordList import PasswordList

class TestMapFromIntermediateToResult(unittest.TestCase):

	def testName(self):
		pass

	def test_FullFunctionality(self):
		print("Running test FullFunctionality on TestMapFromIntermediateToResult.")
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclPasswordList = PasswordList()
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)
		
		lclIntermediate = 77823465
		
		lclStringIntConverter = BasicStringIntConverter()
		lclStringJoiner = BasicStringJoiner(lclStringIntConverter)
		lclCombiner = BasicCombiner()
		lclJoinerAndCombiner = BasicStringJoinerAndCombiner(lclStringJoiner, lclCombiner)
		
		lclCombinedInput = lclJoinerAndCombiner.joinAndCombine(lclPasswordList)
		
		lclDifferenceMapper = BasicDifferenceMapper()
		lclDifferenceMapper.defineMapper(lclCombinedInput, lclIntermediate)
		
		lclMapInputToIntermediate = BasicMapInputToIntermediate(lclDifferenceMapper, lclJoinerAndCombiner)
		lclMapInputToIntermediate.defineMap(lclPasswordList, lclIntermediate)
		
		self.assertEqual(lclMapInputToIntermediate.compute(lclPasswordList), lclIntermediate)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()