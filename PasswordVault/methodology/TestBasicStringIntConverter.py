'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsBasicStringIntConverter import BasicStringIntConverter

class TestBasicStringIntConverter(unittest.TestCase):
	def test_ConversionFunctionality(self):
		print("Running ConversionFunctionality for BasicStringIntConverter.")
		
		#converter = BasicStringIntConverter()
		
		#print("Loosey Goosey")
		#print(converter.toInt("AA"))
		#print(self.convertIntThenString("AA"))
		#print("AA becomes " + self.convertIntThenString("AA"))
		
		self.assertEqual(self.convertIntThenString("fish"), "fish")
		self.assertEqual(self.convertIntThenString("fishfish"), "fishfish")
		self.assertEqual(self.convertIntThenString("@ @"), "@ @")
		self.assertEqual(self.convertIntThenString("fs fs"), "fs fs")
		self.assertEqual(self.convertIntThenString("@@@@ @@@@"), "@@@@ @@@@")
		self.assertEqual(self.convertIntThenString("fish juice"), "fish juice")
		self.assertEqual(self.convertIntThenString("dog"), "dog")
		self.assertEqual(self.convertIntThenString(""), "")
		self.assertEqual(self.convertStringThenInt(0), 0)
		self.assertEqual(self.convertStringThenInt(777), 777)
		self.assertEqual(self.convertStringThenInt(123456789), 123456789)
		
		#logging.debug("fish" + " converts to " + self.convertIntThenString("fish"))
		
		# assert(self.convertStringThenInt(-1) == -1)

	def convertIntThenString(self, pString):
		converter = BasicStringIntConverter()
		tempInt = converter.toInt(pString)
		print(tempInt)
		return converter.toString(tempInt)
	
	def convertStringThenInt(self, pInt):
		converter = BasicStringIntConverter()
		return converter.toInt(converter.toString(pInt))
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	
	unittest.main()