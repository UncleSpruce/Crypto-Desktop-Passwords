'''
Created on Jul 18, 2015

@author: Owner
'''
import unittest
from methodology.clsBasicMapInputToIntermediate import BasicMapInputToIntermediate
from methodology.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList

class TestCombinedMap(unittest.TestCase):

	def sample(self, pInput, pIntermediate, pResult):
		lclMap1 = BasicMapInputToIntermediate()
		lclMap1.defineMap(pInput, pIntermediate)
		lclIntermediate = lclMap1.compute(pInput)
		self.assertEqual(lclIntermediate, pIntermediate)
		
		print("Intermediates")
		print(pIntermediate)
		print(lclIntermediate)
				
		lclMap2 = BasicMapIntermediateToResult()
		lclMap2.defineMap(lclIntermediate, pResult)
		lclResult = lclMap2.compute(lclIntermediate)

		self.assertEqual(lclResult, pResult)

	def test_FullFunctionality(self):
		print("Running Full Functionality Test For TestCombinedMap.")
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclPasswordList = PasswordList()
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)
		
		lclIntermediate = 0
		
		lclResult = "Stormy"
		
		self.sample(lclPasswordList, lclIntermediate, lclResult)


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_FullFunctionality']
	unittest.main()