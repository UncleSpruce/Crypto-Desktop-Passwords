'''
Created on Jul 18, 2015

@author: Owner
'''
import unittest
from primary.clsBasicDifferenceMapper import BasicDifferenceMapper


class TestDifferenceMapper(unittest.TestCase):


	def test_FullFunctionality(self):
		print("Running FullFunctionalityTest on TestDifferenceMapper")
		lclMap = BasicDifferenceMapper()
		lclMap.defineMap(3, 11)
		self.assertEquals(lclMap.compute(3), 11)
		


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()