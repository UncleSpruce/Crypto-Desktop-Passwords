'''
Created on Jul 16, 2015

@author: Owner
'''
import unittest
from primary.clsBasicHash import BasicHash
from primary.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult

class TestMapIntermediateToResult(unittest.TestCase):

	def sample(self, pIntermediate, pResult):
		lclMap = BasicMapIntermediateToResult()
		lclMap.defineMap(pIntermediate, pResult)
		self.assertEqual(lclMap.compute(pIntermediate), pResult)
		
	def test_FullFunctionality(self):
		print("Running test FullFunctionality on TestMapIntermediateToResult.")
		#print(lclMap.compute(7))
		self.sample(5235654324980852804578394785, "password")

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_F']
	unittest.main()