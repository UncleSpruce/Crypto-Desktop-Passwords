'''
Created on Jul 15, 2015

@author: Owner
'''
import unittest
import logging
from primary.clsBasicStringIntConverter import BasicStringIntCoverter

class Test(unittest.TestCase):

	def test_ConversionFunctionality(self):
		converter = BasicStringIntCoverter()
		
		print("Loosey Goosey")
		print(converter.toInt("AA"))
		print(self.convertIntThenString("AA"))
		#print("AA becomes " + self.convertIntThenString("AA"))
		
		assert(self.convertIntThenString("fish"))
		assert(self.convertIntThenString("fish") == "fish")
		assert(self.convertIntThenString("dog") == "dog")
		assert(self.convertIntThenString("") == "")
		assert(self.convertStringThenInt(0) == 0)
		assert(self.convertStringThenInt(777) == 777)
		assert(self.convertStringThenInt(123456789) == 123456789)
		
		logging.debug("fish" + " converts to " + self.convertIntThenString("fish"))
		
		# assert(self.convertStringThenInt(-1) == -1)

	def convertIntThenString(self, pString):
		converter = BasicStringIntCoverter()
		return converter.toString(converter.toInt(pString))
	
	def convertStringThenInt(self, pInt):
		converter = BasicStringIntCoverter()
		return converter.toInt(converter.toString(pInt))
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	
	unittest.main()